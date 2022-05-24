## Azure Functions
Event driven serveless framework based on multiple triggers . 

### characteristics 
- scalable - will scale based on the number of requests 
- stateless - new Invocation will not be able to acess the previous state . 

### selection criteria 
- custom operation should be built 
- functionality already existing in native code ( in programming language )
- involves few api ( mostly a trigger source and response output )


Azure Function can be triggered by 
 - REST  endpoint 
 - Timer Job 
 - message from another service ( ASB ) 

 cost based on 
 - execution count
 - running time for each excution 


## Azure Logic Apps
Low code / No code development tool .

### characteristics
- designed in a web base portal
- Built using large number of connectors.
- custom connectors can be made

### selection criteria 
 - involves multiple popular endpoint or tasks  ( listen to queue , send email , add a record )
 - non avaialability of developer resources 

cost based on 
- execution count 
- cost per connector

## Azure VM

### Connection Azure linux vm 

follow the same steps in [aws docs](https://github.com/dinith72/CodeDocs/blob/main/cloud/aws.md#connecting-aws-ec2) to make the **.pem** file read only.

copy the pem file to path ``` C:\Users\<user>\.ssh ```

type the following command in terminal 
``` powershell 
ssh -i <pem_file_path> azureuser@20.69.160.50
```
