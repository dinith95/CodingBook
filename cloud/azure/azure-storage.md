# Storage Accounts 

## Rules in Creation
- only lowercase letters and numbers can be used 
- should be globally unique 

# Blob Storage 

## rules in Creation
- only lowercase letters numbers and hyphens
- begin with letter or number 

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
- highest storage cost 
- low access cost

> cool tier 
- infrequent aceess data 

> archive 
- lowest storage cost 
- highest access cost
- archival data 
- data should be brought to hot tier before accessing. 

## Life cycle managemnet policy
a policy can be made to automatically move blob from *hot* to *cool* and after that to *archive*.

## Object Replication in Blob [more info](https://learn.microsoft.com/en-us/training/modules/configure-blob-storage/6-determine-blob-object-replication)
- copies the blobs in a container asynchronously to another destination.
- **requires** blob versioning to be enabled on both the accounts. 
- source and destination containers can be in different access tiers. 



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

get the **directory client of folder** which is few levels down the root directory . 

``` c#

const string XmlFolder = "IX/3rd party XML/xmls";
var xmlFolderClient = regSASClient.GetDirectoryClient(XmlFolder); // directly get folder client of specified path
```

download  **file from ```FileShareClinet```** to local storage.

``` c#
// here xmlfolderClinet is the DirectoryShareClient
 var filesClient = xmlFolderClient.GetFileClient($"{documentId}.xml");
var downloadStream = await filesClient.DownloadAsync();

using (FileStream stream = new FileStream(Path.Join(tempFolder,$"{documentId}.xml"), FileMode.Create))
{
    downloadStream.Value.Content.CopyTo(stream); // copy the download stream to local file
} 
```        