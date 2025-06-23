# Kubectl commands 
## auth 

### can-i 
- shows whether you have the permission to perform the action 
- example : `kubectl auth can-i delete pods/<resource-name>`  , <resource-name> is not specified it means all the resources

> check for another user 
- admin privilege is required. 
- add the chunk `--as <user-name>` to the above command 


## Get 

- retrieves the resources 
- command ```kubectl get <resource-type>```
- the output type can be based on the [output-formats](#output-formats----o)

### namespace 
- namespace should be defined if not namespace set as default namespace will be used 

> get items in all namespaces 
- use the commadn `--all-namespaces`

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

    ### a service accunt token 
    - create a service account token and it valid for 1 hour 
    - ``` kubectl create token <service-account>``` 

## config 
- use to change the configerations of the k8s clustes 

> use diffrent cubconfig file 
- default the config file at `$Home > .kube > config` file is used. 
- to change the path of the file use `--kubeconfig` 
  
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

## Exec 
- execute a command inside a pod 
-  ``` kubectl exec  <pod-name> -- <command> ```

###  get to termianl of pod 
- access the terminal of the pod 
- ``` kubectl exec -it  <pod-name>  -- sh ```


## Rollout 
- manage the rollout of the **deployments**

> undo rollout 
 - reverts the current deployment to the previous deployment 
 - ``` kc rollout undo deploy <deployment-name>```
  
### Rollout History 

- view previous deployments / revisions . 
- ``` kubectl rollout history deployment <deplyment-name>```

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

## K8s Multi commands script

```ps1

$filePath = ".\pods.txt"

# Read all lines from the file
$items = Get-Content -Path $filePath

# Loop through and print each item
foreach ($item in $items) {
   & kubectl delete job -n=core-dev3 $item
    Write-Host "Deleted job: $item"
}

```