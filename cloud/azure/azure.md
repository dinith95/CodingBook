## common errors 

### could nt start storage emulator 

this is mostly due to the a **another software using port 10000**.
to resolve :
- find programme using port 10000 by - 
```powershell
netstat -p tcp -ano | findstr :10000
```

- run **terminal** in **admin mode** and kill process 
```powershell
taskkill /PID < process-number > /F
```
  -for  more info refer   [kill a task](../scripting/powershell.md#kill-a-task) in powershell doc 



## Azure storage 



## Azure VM

### Connection Azure linux vm 

follow the same steps in [aws docs](https://github.com/dinith72/CodeDocs/blob/main/cloud/aws.md#connecting-aws-ec2) to make the **.pem** file read only.

copy the pem file to path ``` C:\Users\<user>\.ssh ```

type the following command in terminal 
``` powershell 
ssh -i <pem_file_path> azureuser@20.69.160.50
```
