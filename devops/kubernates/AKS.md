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
