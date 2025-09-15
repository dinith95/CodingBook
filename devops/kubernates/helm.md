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
  
# Helm Chart Tips

## Multiple Templates 

if the same helm template is applied iteratively by changing some values in the helm template , add `---` at the **end of helm template**. 

if not only the last of the jobs will get applied.

```yaml
{{- range  $job := .Values.jobs }}
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cm-tools-runner-{{ $job.name }}
  namespace: {{ $.Release.Namespace }}
spec:
 # rest of the helm file 

--- # marking end of helm template
````



