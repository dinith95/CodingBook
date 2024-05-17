## Introduction
K9s is one of the great ides for managing the Kubernetes clusters 

## Key Combinations 

` : ` - switch between resources 

` / ` - filter the given results ( this result can be anything , pod names , logs , config values)

`ctrl + a` - get list of all the k8s resources 

` d ` - describe about a pod

` shift + (letter) ` - sort the result list by a property ( shift + a - sort by age, shift + m  - sort by memory)

## Commands 

### Pods 

list the set of pods and their properties ( CPU , RAM )

### secrets 

shows the secret values like environment secrets 

## Configurations

### Change Default Editor

to change the default editor to vscode use `$env:EDITOR = "code -w"` in powershell

or to set permanently add that to the **Environment Variables** in windows screen
