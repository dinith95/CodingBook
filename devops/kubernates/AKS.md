## Information 

- AKS manages the deployment and the core managment tasks. 
- only pay for the nodes which run the applications. 

## Componenets of the AKS

![AKS components](https://learn.microsoft.com/en-us/training/wwl-azure/plan-azure-kubernetes-service-deployment/media/kubernetes-architecture-components-fb87cc85.png)

### Virtual network

AKS creates a virtual network which all the agent nodes are connected. 

### Ingress 

- Exposes the HTTP routes to services inside cluster. 

### Azure Load Balancer 

- route traffic to azure ingess 

### Azure Active Directory

- Authenticate the applications and services. 

### Azure Container Registry 

- store the private docker images 

### Azur Monitor 

- collectes and stores the metrics and logs 
- **dashboards alerts** can be created from the data of Azure Monitor. 

## Azure Kubernates Cluster Architecture 

![K8s-cluster-architecture](https://learn.microsoft.com/en-us/training/wwl-azure/plan-azure-kubernetes-service-deployment/media/overview-cluster-nodes-bad6d19a.png)

![control-pane0](https://learn.microsoft.com/en-us/training/wwl-azure/plan-azure-kubernetes-service-deployment/media/cluster-architecture-control-plane-and-nodes-e496ba6d.png)

### Master Node 
- manages which worker nodes are running on the pods 

### Worker Node(s) 
- runs the containalised application workloads . 

### Control Pane 
- runs the scheduling software 

### Kubectl 
- it is a CLI which is used by developers and operators to interact with K8s cluster. 

- commands by the kubectl are send to the **kube-apiserver** . 

- api-server then sends the commands to **controller-manager** which will handle the worker nodes operations. 

### etcd 
- key value datastore storing the current configeration in the k8s cluster. 

## Namespaces 

### Default 
- here the pods and the deployments reside 
- can deploy apps directly to this namespace 

## kube-system 
- core resources exists such as 
    - DNS 
    - proxy 
    - kubernates dashboard 

## kube-public 
- used for resources visible in whole cluster. 

## Storage in AKS 

### EmptyDir 
- temporary space for the pod. 
- all containers can access this volume 
- reside only **lifespan of the pod**. 

### secret 
- inject the pods sensitive data as passwords. 

### Configmap 
- inject the pods **key-value pair** propertese. 

### PersistentVolume 
- block of file storage managed by *Kubernates API* 
- has the ability to perisist beyond the lifetime of the pod. 

## Networking Architecture 

### Hub and Spoke 

- HUb and the Spoke is deployed in *seperate VNETs* 

- HUb contains the 
    - azure firewall 
    - azure bastion
    - azure monitor

- Hub has 3 subnets. 
    - host azure firewall 
    - host gateway 
    - azure bastion

- spoke has 4 subnets 
    - host azure application gateway ( consists of WAF )
    - host ingress resources 
    - host the cluster nodes 
    - host private link endpoints ( connections to Container Registry and Key Vault )

## Autoscaling in AKS 

### Horizontal Pod Autoscaler 

- scales the number of pods in a Node 
-  **max replica count** and **min replica count** should be set. 
- relies on the **Kubernates Scheduler** to assign new pods or delete pods. 

### Cluster Autoscaler 

- AKS add on component that scales the number of nodes. 
- when K8s scheduler fails to create a pod , autoscaler *provisions a new node*. 
- when autoscaler detects unused capacity , pods are moved to another node and node is removed. 

## Azure policy 
- requires 3 new pods to be runnning. 
    - 1 audit pod 
    - 2 webhook pods 

## Azure Initiative
- collection of *Azure-policies* towards specific target. 
- eg : resources to meet the **PCI-DSS** compliance. 