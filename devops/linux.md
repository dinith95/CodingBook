## Installing in Linux 

### Installing Asp .NET core on Linux 


> to install on ubuntu 18.04 LTS

use the below command set 

```shell
wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo add-apt-repository universe
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install -y aspnetcore-runtime-3.1 ## for the version 3.1
```
to get the **runtime versions** repeat above steps with 

```shell
dotnet --list-runtimes ## get the donet runtimes 
```

### Install azcopy tool in linux

follow the commands in the below [github Post](https://gist.github.com/aessing/76f1200c9f5b2b9671937b3b0ed5fd6f) . 

### Install powershell in linux

follow the commands in [microsoft docs](https://docs.microsoft.com/en-us/powershell/scripting/install/install-ubuntu?view=powershell-7.2#installation-via-package-repository)

## Linux Process Management 

### view the current cpu and memory availability 

``` top ``` can be used to view the ongoing processes, cpu usage and memory usage 

### process output tools 

- ```  > ``` - replace the standered output to text file , writes to the file .

Eg => **ping 8.8.8.8 > sample.txt**

- ``` >> ``` - replace the standered output to text file , appened to the file 

- ``` < ``` - gets the content from file to a process 

### process commands 

- ``` & ``` - send a process to background 

- ``` jobs ``` - get all the processes running in the background 

- ``` fg < process id > ``` - get process to the foreground

- ``` kill -9 < process id > ``` - kill a process from that id 


## Linux File managment 

### compress  and extract files 

**tar** command can be used to compress and extract .gz files 

- ```  tar -czvf name-of-archive.tar.gz /path/to/directory-or-file ``` - to compress to **.gz** file 

- ``` tar -xzvf archive.tar.gz ``` - will extract contents in a compressed file 

- ``` tar -xzvf archive.tar.gz -C /dinith/content ``` - w8ill extract contents to a specific folder 



## Linux useful commands 

- ``` wget <url> ``` - download anything from web 

 eg :- ``` wget "https://aka.ms/downloadazcopy-v10-linux" ``` will download the azcopy tool archive from the web . 

- 