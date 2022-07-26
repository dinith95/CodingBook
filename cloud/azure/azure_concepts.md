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


## Azure App service 
HTTP  based service for *Web Applications / REST  Apis / Mobile backends* with build in **Auto Scale** Support.

A [tutorial](https://docs.microsoft.com/en-us/learn/modules/introduction-to-azure-app-service/7-create-html-web-app) to create an host azure web app.

App service provides buillt in Authentication and Aujthorisations with multiple identity providers . 
- [Active Directory](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad) 
- [Facebook](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-provider-facebook)
- [Google](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-provider-google)
- [Twitter](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-provider-twitter)

### Feature Flags 
Boolean values which will decide the excution off a feature based on provided conditions. 
 feature manager support *appsettings.json* to configure the features as shown . 

 ``` json 
 "FeatureManagement": {
    "FeatureA": true, // Feature flag set to on
    "FeatureB": false, // Feature flag set to off
    "FeatureC": {
        "EnabledFor": [
            {
                "Name": "Percentage",
                "Parameters": {
                    "Value": 50
                }
            }
        ]
    }
}

```

### Autoscaling 

Increase the number of resources based on the diffrent metrics exceeded by a server as defined by user . 

eg -> user can design an web service to autoscale if the memory usage in > 80%. 

always increase *the number of servers* will not scale vertically. 

**scale in** - reduce the number of instances. 
**scale out** - increase the number of instances. 

Types of auto scales supported 

- metric based - based on a monitored matrci ( HTTP request waiting / messages in a queue / CPU ) - [all metrics](https://docs.microsoft.com/en-us/learn/modules/scale-apps-app-service/3-app-service-autoscale-conditions-rules#:~:text=Metrics%20for%20autoscale%20rules)

- schdule based - schdule to autoscal during a timeperiod ( 6pm - 8 pm / Sunday)

**Autoscale Conditions** - [more info](https://docs.microsoft.com/en-us/learn/modules/scale-apps-app-service/3-app-service-autoscale-conditions-rules#:~:text=has%20been%20crossed.-,Autoscale%20actions,-When%20an%20autoscale)

Multiple autoscale rules can be defined for the same autoscale condition . 

eg : sample rules 

- if HTTP Queue > 10 => scale out by 1 
- if CPU > 70% => scale out by 1 
- if HTTP Queue = 0 => scale in by 1
- if CPU < 50% => scale in by 1

> scale out => Any of the conditions should be met ( HTTP queue > 10 | CPU > 70%)

> scale in => All the conditions should be met ( HTTP queue == 0 && CPU < 50%)

**AutoScale flapping avoidance**

Azure would try to avoid the system **would scaling in** if it has to scale out immediately after it scaled in .  - [more](https://docs.microsoft.com/en-us/learn/modules/scale-apps-app-service/5-autoscale-best-practices#:~:text=Choose%20the%20thresholds%20carefully%20for%20all%20metric%20types)



## AKS - Azure Kubernates Service 

Microsoft managed kubernates service 

> master node is managed by **Azure**

> Azure vms can be used to deploy the worker nodes . 

> only billed for the running agent pool nodes.


## ACI - Azure Container Instances 

Instantly host an docker image in a container without worrying about the underlying infrastructure. 

## ACR - Azure Container Registry 

> store the image information regard to the Azure container Images. 


## Azure Batch Services 

> cloud based job schduling tasks 


## Azure Cosmos Db 

used to store the document type data ( No SQL type data ). 


### document  

each record is an **Json object** .

it has following metadata. 

- etag 

- _ts  shows the time which the document has last updated . it will be shows in  epoch time . [more info](https://stackoverflow.com/a/73123605/8313114)
