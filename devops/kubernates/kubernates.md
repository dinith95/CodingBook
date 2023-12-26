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

 ## Manage the contexts 

 Get list of contexts - ```kubectl config get-contexts```

Get the current contexts - ```kubectl config current-context```

change context - ```kubectl config use-context <context>```

 ### Get logs of a pod

 basic command : ``` kubectl logs -n < namespace> < pod-name > -f ```

 parameters information 

 - -f => this will show the logs continuously. 