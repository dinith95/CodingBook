# intro
Helm chart Has the files and the configurations to define how the applications install in the K8s  environment.

# Helm Commands 

## Install helm chart 

```helm
helm upgrade --install  <chart-name> <helm-folder> -f <values-file> --namespace <namespace> 
```

 - chart-name - name which the service is installed in the k8s 
 - helm-folder - folder containing the helm files  information 
 - values-file - file containing the values for the helm
 - namespace - k8s namespace
 - --debug - this will list the logs of the execution of the helm update
  
  


