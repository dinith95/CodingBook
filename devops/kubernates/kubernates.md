
# container types  

## init Containers  
 - use to excute some task in the startup and exit the container 
 - run **before the default containers startup** 
 - each init container **should complete before other init container** starts 
 - if any container failed the pod will restart 

### Diff compared to Sidecar 

- Init containers run before the main container start , sidecar run laong with the main container 

# Container  Probes 

### Readiness Probes

- defines some conditions such that the pod is marked as ready in pod states 
- eg : http get request to the web api , only that becomes success pod will be marked as ready 
- default **3 equests will be made** but can be overridden by `failureThreshold` 

### Livenes Probes 

- to check the application is running healthy 
- eg : http get request to an endpoint in application , if request dosent return success the container will be restarted . 

# Admission controllers 
- intercept the request  *after the authorization* but before the *creation of the request*. 
- only works with the **create / delete / modify** objects
- to find **enabled admission controllers**  , check `--enable-admission-plugins` in the pod `kube-apiserver-controlplane` 

## Add / Remoe Admission controller plugins 

- go to the location `/etc/kubernetes/manifests` and edit file `kube-apiserver.yaml` 
- **enabel** a plugin - add to the attribute `--enable-admission-plugins`
- **disable** a plugin - add to the attribute `--disable-admission-plugins`

## Admission controller types  
  - **validating** - validate existing controller request and accept / reject request 
  - eg : `NamespaceExists` - check if the namesapce exists and accept / reject request based on that 

  - **mutating**  - change the exisitng controller request 
  - eg : `AlwaysPullImages` mutates the **image pull policy**

> Note - Mutating admissing controls run prior to the vallidating admission controls 

## Custom Mutation / Validation controllers 
- custom controllers can be created to mutate or validate user request 
- can be achived through `webhook server` 

# Pods 

 - pods are the smallest unit that the **K8s Manages** . 
 - pods can contain **1 or more containers** but in most cases **1container only**. 
 - are a logical resource. 

# Namespaces 

- pods are collected / grouped into namespaces . 
- limits to the resource usage can be set in namespaces. 

# Nodes 

- nodes are physical or virtual vms that are running the k8s . 

> master-node - it is the brain of kubernates , controls all the actions of the k8s

> worker nodes - pull container images and runs the pods 

# controlers 

 - track the resources and keep resources as per the users description

 eg : no of pods / version of software running in a pods 

# Replica set ( Replication Controller - old tech) 

 - ensure the specified number of pods are runnning . 
 - f a pod goes down Replica set will create another pod. 
 - replicaSet has a selector which applies to pods having a perticular label

  ### Load Balacing 
  - will create more pods if there is too much load on the current system

# Deployments  
- they does the similar function of the replica-set , maintain specified set of instances running at any given time . 
- also they help to manage the 
  - updates to pods ( like new image version ) in a rolling manner 
  - can rollback to the previous version ( revision )

### Deployment Strategy 
- 2 deployment startegies 
- **Default startegy - RollingUpdate**
  - `Recreate` -  will remove all the pods and create new ones 
  - `RollingUpdate` - will remove one pod and deploy the new pod from the new version

### Blue / Green deployment strategy 
- here 2 identical production envs are run in parallel 
- this can be achieved by kubernetes through a work around 

> steps 
 - create a new deployment with a new label 
 - once pods a up perform the tests 
 - then from service redirect all traffic to the new service 

### Canary deployment 
- small portion of the traffic is directed to the new service 

> steps 
 - create the new service with the same label / selector 
 - but keep the pod count to a minimum in the new deployment ( preferred 1 )
 - once test are successful , **increase the pod count ** in new deployment and in previous deployment make it 0


# DNS  - Acessing Services 

### Full path 
any service will be having the following path patter  `db-srvice.dev.svc.cluster.loacal` , the above path can be broken down to . 

`db-service` - service name 
`dev` - namespace 
`svc` - service 
`cluster.local` - domain 

Services outside the **namespace** should use the **full path** to access. 

# Configmaps 
storing the configeration information . 
config map definiton file - [definiton file](https://kubernetes.io/docs/concepts/configuration/configmap/#configmaps-and-pods) . 

cofigmap can be refrred in multiple ways 

### As Env Variable 

Pod can refer the config value as an env variable from the configmap 

they are not updated automatiacally and need periodic restart 

``` yaml
env:
 - name: PLAYER_INITIAL_LIVES  # name of the env variable                 
   valueFrom:
      configMapKeyRef: # reference to the configmap 
        name: game-demo           
        key: player_initial_lives
```

### As Volume 
- volume should be added to the pod spec 
- reference to that volume should add as `volumeMounts` 

``` yaml
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo # add the volume to volume mount
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    configMap: ## add my configmap as a volume with name foo 
      name: myconfigmap
```

# Secrets 
- can be use store secret values with encoded data 
- secrets are not encrypted but it is **base 64 encoded**
- not best method to store key and confidential info as secrets are only encoded 

## create secret 
- can be created in the imprative way
``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: dotfile-secret
data:
  secret-file: dmFsdWUtMg0KDQo= # added base64 encoded manner 
```

## Binding secrets

### from secret key ref 

- can be bound to  as **env variable** at the **container level**

``` yaml 
 env:
  - name: MYSQL_USER
    valueFrom:
      secretKeyRef:
        name: db-user
        key: username
```

### as a volume 
- should be added as volume in pod 

``` yaml
volumes:
    - name: secret-volume
      secret:
        secretName: dotfile-secret # name of the secret 
```
- it should be added in colume mounts in container 

``` yaml
volumeMounts:
      - name: secret-volume # match the volume name in the pod
        readOnly: true
        mountPath: "/etc/secret-volume"
```

# security context 

- defines the security related attributes for the pod and containers running in the pod . 

### Run As User 

- defines the user role which the processes in the pod will execute 
- by default it is `root` ( `userId: 0`)
- can be configured on **Container and pod level**
- configeration on container **takes precedence**

### set up capabilities 

- can grant certain priviledges with granting all the priviledges of the linux . 
- capabilities can be modified as shown below.

``` yaml

securityContext:
      capabilities:
        add: ["NET_ADMIN", "SYS_TIME"] ## add capabilities 
        drop: ["NET_RAW"] ## remove capabilities 
```

# Services 
- enable the connection within the k8s cluster  and also resource groups and outside entities. 
  
eg : **within cluster** - front end service connect to back end service 
    **outside cluster** - backend services connect to database 

## Nodeport Services 
- allows **external application to access a pod** using a port open to external service. 
- more information [k8s docs](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)
  
> nodeport service architecture 
 - **target port** is set to the same value as port by default and as a practice 
 - **node port** - k8s control plane will allocate a port  if not set 
  
![nodeport service](/images/nodeport-service.jpeg)

> service endpoints 
 - the pods  that services send traffic to

## Cluster-IP Service 
- default type of service 
- **map pods with multiple ips** to a single service. 

> port definitions 
- `port` - the port of the service 
- `targetPort` - the port of the application 
  
# Ingress 

Ingress does multiple functions 
- functions as HTTPS 
- act as a load balancer 
- act as proxy server 
- url based routing configs 

### Ingress resources 
- set of rules defined for ingress service. 
- there are **2 types**
  
> rewrite target 
 - this will replace the url segment by the value provided here 
 - if this is not set the url will be directly forwarded to the clinet app but client app will not have that url configured 
  
**template** - placed under `metadata`

``` yaml
annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
```

**example**
  - app url - `https://www.app1.com/live/home` this will forwarded to `live-service`  as `https://www.app1.com/live/home` ( unchaged )
  - but when **rewrite-target** is set to `/` it will be forwarded as `https://www.app1.com/home`

### Ingress Resources -  path 
- redirect the routing thorugh the path 
- sample [ingress-path-template](https://gist.github.com/dinith95/8a6a4ae9ab0c160134852f00e8618834#file-resource-by-path-yaml)

### Ingress Resources - host 
- redirect the routing through host 
- sample [ingress-host-template](https://gist.github.com/dinith95/8a6a4ae9ab0c160134852f00e8618834#file-resource-by-host-yaml)

### Ingress Controller 
- executes the rules defined by the Ingress resources 
- k8s does not have default ingress controller

following services need to be deployed 
- deployment 
- nodeport service 
- configmap
- service Account


# Service Account 

- use by applications to access the resources
- eg : prometheus use to get the metrics in k8s 
- the client application is hosted in the k8s the service account can be **mounted as a projected volume** .  
- service account tokens will have a 
  - expiration time 

### Service account tokens 
- service account tokens are created and stored as a secret object 

### default service account 
- any namespace a default service account exists 
- when a pod is created default service account is mounted 

# Resource Requirements 

- the amount resources used by the pod / container  
- **1 unit of cpu** - 1 core in azure  / 1 vCPU in AWS 
- **1 Gi** - 1024 Megabytes of memory
- **1 G** - 1000 Megabytes of memory 
- by default values are not set for the cpu and memory 
  
### Resource Requests 
- this is the minimum requirement to start that perticular pod 
- eg : pod having 1 Gi memory should have a node which is more than 1 Gi of memory free 
- after the creation of the pod , it can scale up as required 

### Resource Limits 
- **maximum resources** that can be taken by a pod. 
- eg : pod having 2 Gi memory , can scale upto 2Gi

### Limit Range 
- use to set values for all pods , if the values are not specified  
- it is only applicable for pods created after limit range is set 
- following values can be set 
  - **default** values , if not specified for a pod 
  - **max and min** values 
- if a pod exceeding the min or max limit is attempted to create,  it throws an error . 

### resource quotas 
- configured at namespace levels 
- set maximum **requests and limit amount** for the namespace 

# Taints and Toleration  

### Taints
 -  defined on **node** 
 -  allowing only certain type of pods are to be scheduled  on that node 
 -  for the pod to be schduled pod should meet that criteria
 -  eg : taint : appName should be `WebApp` 
    -   ```kubectl taint nodes <node> appName=WebApp:<effect>```
-   There are 3 **Effects**
    -   `PreferNoSchedule` - scheduler will try to avoid scheduling of the pods which dosent match the taint 
    -   `NoSchedule` - no new pods will be scheduled on that node which dosent match the taint 
    -   `NoExecute` - affects current pods on the node which does not matched the taint , those pods are evicted . 

### Toleration
- specific property which allows pods to be scheduled in **tainted node**
- eg : appName=WebApp 



# Node Selector & Node Affinity

### Node Selector
- pod can be configured to run on a specific node matching the label 
-  limited in scope as it only work with simple match 
-  eg; place only on nodes with `Large` label
``` yaml
nodeSelector:
    disktype: Large
```

### Node Affinity 
- this does the same thing but can support more complex logic 
- eg: nodes having either labels `Large` or `Medium` 

### Affinity Types 

> requiredDuringSchedulingIgnoredDuringExecution
 - during scheduling there **should be a node matching criteria**
 - unless pod is not scheduled

> preferredDuringSchedulingIgnoredDuringExecution
- during scheduling scheduler try to match the criteria 
- if none found it will schedule on available node 

> operator types 

- IN - label value preset in set of values supplied 
- NotIn - label value not present in supplied values 
- Exists - label with key exists 
- DoesNotExists - label with this key does not exists

sample affinity 
``` yaml
affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: size
            operator: In
            values:
            - Large
            - Medium
```


# Persistent Storage  
- storage that use to store the data in permamnant manner 
- in the pod storage the data will be deleted when the pod is deleted 

## Persistent volume ( PV )  
- storage entity provisioned by the admin with 
  -  size 
  -  storage class 
  -  accessMode 
- pvc are **bound** to the pv **if the criteria is matching** 
- pv definition template [k8s docs pv](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/#create-a-persistentvolume)

> Retention Behaviour 

- **Retain** - pvc is delete pv will continue to exist but cannot be assigned to new **pvc directly**
- **Delete** - pv is deleted once **pvc** is deleted. 
- **Recycle** - remove all the data and makes it available for new volume 
  
## Persistent Volume claims  ( PVCs)

- these are request made by user requesting a pv 
- pvc bind to a pv 
- **pvc can only bind to singe pv and vice versa**
- pvc definition template [k8s docs pvc](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/#create-a-persistentvolumeclaim)

> Requirements to satisfy to bind to pv for pvc 

- size of pvc <  size of pv 
- same `accessModes` 
- same `storageClass` 

> adding pvc to a pod 
 - pvc is added using below template in **spec > volume**

```yaml
 volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim # name of the pvc 
```
## storage class 
- duynamic provision
- volume get provisioned only **application requires a volume** when the pvc is created 
- storage class definition [k8s docs sc](https://kubernetes.io/docs/concepts/storage/storage-classes/#storageclass-objects)

> pvc using the storage class 
 - add the **storage class info** in `spec` of the pvc 
  
  ```yaml
  storageClassName: azure-disk-level-1 # name of the storage class created 
  ```

# user management 

## kubeconfig 
- stores the information related users , clusters 
- present in the `$Home > .kube > config` 

Has 3 sections 

> Clusters 
- information about the kubernates clusters 
- eg : test-k8s , dev-k8s 

> Users 
- diffrent users present 
- eg : admin / devops lead / engineer 

> contexts 
- match the clusters for users 
- eg : user devops lead cluster dev-k8s 

sample context 
```yaml
contexts:
- context:
    cluster: ckad-test-cluster
    user: clusterUser_ckad-tutorial_ckad-test-cluster
    namespace: default
```

# Authorization

## ABAC ( Attribute Based Authorization )
- create a policy file and should be passed to the **kube api server**
- the policy document should be created in json format , [samples](https://kubernetes.io/docs/reference/access-authn-authz/abac/#examples)
- for any changes the **file should be edited manually** and server should be restarted. 

## Role Base Access Controls 
- Role is created with set of permissions 
- eg : `dev` role with **all access to pods**. 
- then users / user groups are assigned to that role 

### Role Object 
- defines the capabilities of the role ( what a user having the role can do and cannot do ). 
- sets **within namespace**
- example role - developer role [dev role object](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-example)
- for **granular resource filter** the resourcename can be used as `resourceNames: ["fin-app1"]`
- **api group: empty** means the core api group , if its other api group it should be specified. 

### Role Binding Object 
- binds **developer user** to a **role**. 
- sample role binding : [role binding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-example)

### cluster roles 
- create clusterwide ( common to complete cluster )
-  use to grant access to the cluster scoped resources ( nodes secrets )
-  if the resource is namespace wide resource, it will **grant access** for type of resource in **all namespaces**
-  eg : if cluster role with **view for pods** is created it can `view any pod in any namespace` of that cluster. 
-  sample role bind [cluster role](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#clusterrole-example)

### cluster role binding 
- grant the permission across the whole cluster 
- cluster role binidng [cluster-role](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#clusterrolebinding-example)
  
## WebHook 
- use 3rd party tool to administer the authorization 

