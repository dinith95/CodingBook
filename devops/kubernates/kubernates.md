## Kubernates concepts 

### Pods 

 - pods are the smallest unit that the **K8s Manages** . 
 - pods can contain **1 or more containers** but in most cases **1container only**. 
 - are a logical resource. 

### Namespaces 

- pods are collected / grouped into namespaces . 
- limits to the resource usage can be set in namespaces. 

### Nodes 

- nodes are physical or virtual vms that are running the k8s . 

> master-node - it is the brain of kubernates , controls all the actions of the k8s

> worker nodes - pull container images and runs the pods 

### controlers 

 - track the resources and keep resources as per the users description

 eg : no of pods / version of software running in a pods 

### Replica set 
 tell how many instances of the pods should be running . 

 if 1 pod goes down Replica set will create another pod. 

## Kubectl commands 

 ## Create 

 - use to create a new pod or a service 

### arguments 

    ```-f``` - specify the yaml file path

## apply 

- apply the configuration to a pod / deployment existing in the cluster 
- it will update the pod / deployment 

### arguments 
    ```-f``` - yaml file path 


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
