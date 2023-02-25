# Blob Storage 
way of storing large untructured binary object ( blobs) . 

it supports a folder structure but it is purely **vitual folders**. 

## diffrent types of blob

> block blobs 

- support **standered storage**
- data is stored as blocks 
- block max size : 100MB
- store dicrete large binary data

> page blobs 
- 512 bytes pages 
- can fetch data from the random pages

> append blobs 
- blocks can be added to the end of the blob

## acess tires of a blob 

> Hot tier 
- frequent access data 
- highest cost 

> cool tier 
- infrequent aceess data 

> archive 
- lowest cost 
- archival data 
- data should be brought to hot tier before accessing. 

a policy can be made to automatically move blob from *hot* to *cool* and after that to *archive*.

# File share storage 

provide a common shared storage for the files so that multiple users can access it. 
- 100Tb of data 
-2000 connections per file 

### perfomance tiers 

> standered 

- stored in a hard disk 

> premium tier 

- stored in ssd 
- greator throughput

# Azure tables 

used to store the semi structured data. 

- a table row must have
    - a partion key
    - unique key

- does not have concepts like *forign keys, relationships, view* 
- containes denormalised data
- when querying bot partition and row key should be passed.


# storage sdks and connections


## .net sdk for storage 

### connect to storage from SAS 

connect to file storage through a SAS token. 

```c#
// pass sas token enclosed in Uri
var sc = new ShareClient(new Uri(config[sasKey]), null);
 var directory = sc.GetDirectoryClient("firectory1"); // path to the directory
```