# Terraform Basics

## Input Variables

Declared in `variables.tf`. Define what inputs your config accepts.

```hcl
variable "cluster_name" {
  type        = string
  description = "AKS cluster name"
  default     = "cube-aks"

  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "Must be dev or prod."
  }
}
```

**Types:** `string`, `number`, `bool`, `list(string)`, `map(string)`, `object({...})`  
**No default** = required at apply time. **With default** = optional.  
Referenced as `var.cluster_name`.

---

## Output Variables

Declared in `outputs.tf`. Expose values from your config to the terminal, remote state, or parent modules.

```hcl
output "cluster_fqdn" {
  value       = azurerm_kubernetes_cluster.main.fqdn
  description = "AKS cluster FQDN"
  sensitive   = true   # hides from plan output and logs
}
```

> **Warning:** `sensitive = true` hides from logs but the value is still in the state file in plaintext. Use remote state with encryption for real secrets.

Referenced as `terraform output cluster_fqdn` from the CLI, or `module.name.cluster_fqdn` from a parent module.

---

## `.tfvars` Files

Assign values to declared variables. Not declarations themselves — just data.

| File | Loaded how |
|---|---|
| `terraform.tfvars` | Auto-loaded always |
| `*.auto.tfvars` | Auto-loaded alphabetically |
| `prod.tfvars` | Explicit: `-var-file=prod.tfvars` |

**Common pattern — per-environment files:**

```bash
terraform apply -var-file=terraform.tfvars -var-file=prod.tfvars
# Later file wins on conflicts
```

**Never put secrets in `.tfvars`.** Use environment variables instead:

```bash
export TF_VAR_db_password="..."
terraform apply
```

`TF_VAR_*` maps automatically to `var.*`.

---

## `resource` vs `data`

| | `resource` | `data` |
|---|---|---|
| Creates / updates / destroys | ✅ | ❌ |
| Reads from Azure | ✅ | ✅ |
| `terraform destroy` affects it | ✅ | ❌ |
| Reference prefix | `azurerm_thing.name.id` | `data.azurerm_thing.name.id` |
| Use when | You own the lifecycle | It already exists |

**Rule of thumb:** who created this thing?
- You (in this config) → `resource`
- Another team, another config, Azure itself → `data`

**Cross-team pattern:** Cloud Engineering owns `resource "azurerm_kubernetes_cluster"`. KB team reads it with `data "azurerm_kubernetes_cluster"` — no ownership, no destroy risk.

---

## Reading Secrets from Key Vault

```hcl
# Find the vault (already exists)
data "azurerm_key_vault" "main" {
  name                = "cube-kv-prod"
  resource_group_name = "rg-cube-prod"
}

# Read a secret
data "azurerm_key_vault_secret" "db_password" {
  name         = "sql-db-password"
  key_vault_id = data.azurerm_key_vault.main.id
}

# Use it
resource "azurerm_mssql_server" "main" {
  administrator_login_password = data.azurerm_key_vault_secret.db_password.value
}
```

**Reading multiple secrets efficiently — use `for_each`:**

```hcl
data "azurerm_key_vault_secret" "secrets" {
  for_each     = toset(["sql-password", "api-key", "cosmos-key"])
  name         = each.value
  key_vault_id = data.azurerm_key_vault.main.id
}

# Access: data.azurerm_key_vault_secret.secrets["api-key"].value
```

**Gotcha:** data sources run at plan time. If you're creating a Key Vault and reading from it in the same config, reference the `resource`, not a `data` block — Terraform will sequence correctly.

```hcl
# RIGHT — references the resource directly
data "azurerm_key_vault_secret" "password" {
  key_vault_id = azurerm_key_vault.main.id   # not data.azurerm_key_vault.main.id
}
```

---

## File Layout

```
├── variables.tf          # Input variable declarations
├── outputs.tf            # Output value declarations
├── main.tf               # Resources
├── locals.tf             # Computed local values (reused, not exposed)
├── versions.tf           # Provider version pins
├── terraform.tfvars      # Common values (committed)
├── dev.tfvars            # Dev-specific values
├── prod.tfvars           # Prod-specific values
└── secrets.tfvars.json   # ← gitignore this
```
