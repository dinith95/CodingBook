## common tricks 

### connecting aws ec2

you can connect to the *aws ec2* instance by the commandline through **SSH**. A *.pem* file is needed . 

> execute following commands when connecting from windows.

```powershell
## reset the permission 
icacls.exe .\test.pem /reset  

# Give current user explicit read-permission
icacls.exe .\test.pem  /GRANT:R "$($env:USERNAME):(R)"

# Disable inheritance and remove inherited permissions
icacls.exe .\tests.pem /inheritance:r

```
