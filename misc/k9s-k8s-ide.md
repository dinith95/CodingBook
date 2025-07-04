## Introduction
K9s is one of the great ides for managing the Kubernetes clusters 

## Key Combinations 

` : ` - switch between resources 

` / ` - filter the given results ( this result can be anything , pod names , logs , config values)

`ctrl + a` - get list of all the k8s resources 

` d ` - describe about a pod

` shift + (letter) ` - sort the result list by a property ( shift + a - sort by age, shift + m  - sort by memory)

## Commands 

### info 
command - `k9s info` 

shows the list of configurations to the terminal

### Pods 

list the set of pods and their properties ( CPU , RAM )

### secrets 

shows the secret values like environment secrets 

## Configurations

### Change Default Editor

to change the default editor to vscode use `$env:EDITOR = "code -w"` in powershell

or to set permanently add that to the **Environment Variables** in windows screen

### Update table columns 

create a `views.yaml` in the root of the k9s folder. 
add values as shown in the following docs [k9s doc](https://k9scli.io/topics/columns/)

> some specific attributes can be specified using the `|` command 