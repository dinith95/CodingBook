## common tricks 

### connecting aws ec2

you can connect to the *aws ec2* instance by the commandline through **SSH**. A *.pem* file is needed . 

> execute following commands when connecting from windows.

```powershell

# assing the pem file name 
 $varPem = ".\ec2test.pem"

## reset the permission 
icacls.exe $varPem /reset  

# Give current user explicit read-permission
icacls.exe $varPem  /GRANT:R "$($env:USERNAME):(R)"

# Disable inheritance and remove inherited permissions
icacls.exe $varPem /inheritance:r

```
