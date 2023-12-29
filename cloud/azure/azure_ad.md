## Managed identities 

- identity is created for azure application ( eg: VM , Function )
- that identitity is like user in AD
- roles and permissions can be assigned to the managed identity 
    eg : Contributor role for SQL server can be assigned to managed identity created for VM 

### System assigned managed identity 

- bounds to the resource 
    eg: if managed identity is created for VM , once the VM is removed identity is also removed 

- cannot be assigned to another resource. 
    eg: managed identity created for *VM01* cannot be assgned to *VM02* . 

### manual attached managed identity 

- not bounded to resource , can be assigned to multiple resources. 
    