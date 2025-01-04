# Kubectl commands 

## Get 

- retrieves the resources 
- command ```kubectl get <resource-type>```
- the output type can be based on the [output-formats](#output-formats----o)

### Arguments 

- ```-l``` - gets pods filterd by a label 
- ```-n``` - get pods filtered by namespace ( not specified will return default )

## Create 

 - use to create a new pod or a service 

    ### arguments 

    ```-f``` - specify the yaml file path

    ### configmap 

    `--from-literal` - this allows us to pass the configs as string 

    sample : create config for app color 
    ``` --from-literal=APP_COLOR=darkblue```

## Apply 

- apply the configuration to a pod / deployment existing in the cluster 
- it will update the pod / deployment 

### arguments 
    ```-f``` - yaml file path 

## Scale 

### Scale Replicaset 
- use to scale the ReplicaSet  
- command , can use any 
  -  ```kubectl scale --replicas=<count> rs/<replica-name>```
  -  ```kubectl scale --replicas=6 -f <file-name> ```

## Edit 
- use to edit kubernetes resources 

### Replicaset 
- edit the details of a replicaset 
- note : if the image is changed it wont impact existing pods running , so that those pods has to be recreated. 

## Quick tips 

### output formats - `-o`

there are several output formats the kubectl support can be specified with `-o` 

- default - human readable format 
- `-o wide` - human redable format with additional info
- `-o json` - json output 
- `-o name` - prints only the name 
- `-o yaml` - prints the output yaml file 


### use dry run 

 - this will create sample yaml file for a kubectl command with the changes 
 - used with the ```kubectl run``` 
  - eg : ```kubectl run redis --image=redis --dry-run -o yaml```  - this will output yaml file to create redis container from the redis image 

### Get logs of a pod

basic command : ``` kubectl logs -n < namespace> < pod-name > -f ```

parameters information 

- -f => this will show the logs continuously. 

### Manage the contexts 

Get list of contexts - ```kubectl config get-contexts```

Get the current contexts - ```kubectl config current-context```

change context - ```kubectl config use-context <context>```

### Get the yaml file of resource

use the command ```kubectl get pod <pod-name> -o yaml```