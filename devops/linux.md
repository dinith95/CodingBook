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
