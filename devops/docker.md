## installing docker 

### installing in ubuntu / aws ec2
Follow the steps mention in the [digital ocean docker install guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) **until step 2**

Run below command to run **test container of docker**

```
    sudo docker run hello-world
```

it will show *hello from docker* message . then docker installation is successful.

Follow step 2  of the install guide , add the current user to docker group 
Note => instead of the su - ${USER} ,  logout and log in 


## docker concepts 


### image 


docker image is developed application with the its packages and the files bundled together . normally dokcer image has 

 - main framework libraries ( .net core runtime)
 - application resources ( dll libraries )
 - congigeration files ( appsetting,json)

[more info ](https://docs.docker.com/engine/reference/commandline/images/)

### registry 

registry is the place where to store the docker images and share with others.

### container 

container is created from the docker base image with application or other process running on it. [more info](https://www.docker.com/resources/what-container/#:~:text=A%20Docker%20container%20image%20is,tools%2C%20system%20libraries%20and%20settings.)


## docker useful commands 

delete single image -   ```docker image rm```

Remove all the images without an container - ```docker image prune -a```

Stop all containers - ```docker stop $(docker ps -a -q)```

connect to docker instance terminal - ```sudo docker exec -it sql1 "bash"``` 

- *sql1* - docker instance name 



## Configuring MS_SQL_sever instance in docker
Complete the [Installing docker in AWS](#installing-in-ubuntu-/-aws-ec2) section

### set up docker instance 
run below command to get sql server instance 

```dockerfile
sudo docker pull mcr.microsoft.com/mssql/server:2019-latest
```

start the sql container by 

```dockerfile
sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=xxxxxx" \
   -p 1433:1433 --name sqlDj1 -h sqlDj1 \
   -d mcr.microsoft.com/mssql/server:2019-latest
```

here :
- *ACCEPT_EULA* - accepting the end user agreement 
- *SA_PASSWORD* - set the sql server database pw 

do a  ```docker ps -a``` and there should be instance with **sqldj1**

### connect to docker instance 

connect to the docker instance by  - ```  sudo docker exec -it sql1 "bash" ```

connect to the *sql command* by 

``` 
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "xxxxxx"
```

here 
 - -P -  password for the sql user instance 

 **notes**  

- When connecting from remote make sure *port 1433 , is allowed* on inbound ports of VM
- useful link - [Microsoft sql server docs](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash)

