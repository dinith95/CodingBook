## Azure VM

### Connection Azure linux vm 

follow the same steps in [aws docs](https://github.com/dinith72/CodeDocs/blob/main/cloud/aws.md#connecting-aws-ec2) to make the **.pem** file read only.

navigate to the folder where pem file is situated

type the following command in terminal 
``` powershell 
ssh -i <pem_file_path> azureuser@20.69.160.50
```