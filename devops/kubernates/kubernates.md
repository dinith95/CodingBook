# Kubernates concepts 

## Pods 

 - pods are the smallest unit that the **K8s Manages** . 
 - pods can contain **1 or more containers** but in most cases **1container only**. 
 - are a logical resource. 

## Namespaces 

- pods are collected / grouped into namespaces . 
- limits to the resource usage can be set in namespaces. 

## Nodes 

- nodes are physical or virtual vms that are running the k8s . 

> master-node - it is the brain of kubernates , controls all the actions of the k8s

> worker nodes - pull container images and runs the pods 

## controlers 

 - track the resources and keep resources as per the users description

 eg : no of pods / version of software running in a pods 

## Replica set ( Replication Controller - old tech) 

 - ensure the specified number of pods are runnning . 
 - f a pod goes down Replica set will create another pod. 
 - replicaSet has a selector which applies to pods having a perticular label

  ### Load Balacing 
  - will create more pods if there is too much load on the current system

## Deployments  
- they does the similar function of the replica-set , maintain specified set of instances running at any given time . 
- also they help to manage the 
  - updates to pods ( like new image version ) in a rolling manner 
  - can rollback to the previous version ( revision )

