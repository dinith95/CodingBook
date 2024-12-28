# Kubectl commands 

## Create 

 - use to create a new pod or a service 

    ### arguments 

    ```-f``` - specify the yaml file path

## apply 

- apply the configuration to a pod / deployment existing in the cluster 
- it will update the pod / deployment 

### arguments 
    ```-f``` - yaml file path 

## scale 

### Scale Replicaset 
- use to scale the ReplicaSet  
- command , can use any 
  -  ```kubectl scale --replicas=<count> rs/<replica-name>```
  -  ```kubectl scale --replicas=6 -f <file-name> ```

## Quick tips 

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