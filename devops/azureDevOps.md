## Pipeline Creation 

### Consuming Artifacts from Different Porjects 

If you have a project named A  and its pipeline needs to consume an artifacts of the project B . 

steps : 

- Add project A build service to the *project B* relavant feed's settings. 

- disable the following settings in the 
*Project A => project settings => settings* as shown below . 

![disable settings](https://i.stack.imgur.com/JlyB4.png)


> Note - when enabled this settings allows  the pipeline of the project to access the nugget feeds of the project only. 

more info can found [stackoverflow answer](https://stackoverflow.com/a/64852034/8313114)