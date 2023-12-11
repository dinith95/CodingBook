# Storage Accounts 

## Rules in Creation
- only lowercase letters and numbers can be used 
- should be globally unique 

## Redudancy Options 

- LRS 
    - 3 copies are maintained in the same data center 
    - redudancy against the server failures. 

- ZRS 
    - copy is replicated within each of the **3 avaialability regions**.

- GRS 
    - data is copied 3 times in the primary data center using the LRS 
    - Data is **asynchronously** copies to another region. 
    - in a case of failure this would become the new primary region.

- GZRS 
    - copies data *sycronously* to 3 azure avaialability zones. 
    - *asyncronously* copies data to another region.


## Authorisation 
authorisation can be given by many starategies. 

- Microsft Entra ID - RBAC access can be given for each of the storage services 
- shared Key - access keys to the storage account 
- SAS toekn - delegates access to specific resource with specific permission and for specified time interval 
- anonymous access - 

### Autherisation from Stored Access Policies

- storead access policies can be created 
    - blob container 
    - table
    - file share 
    - queue 
- An SAS can be created defining the access policy
- permission and expiry time can be defined. 
- compared to default SAS these permissions can be revoked or changed when required. 


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

## Blob Data Retension Policy 
support the policy ```Write once read many ``` for immutable storage. 
- blob can be transffered within diffrennt *access tiers* while holding the immutability

### Time based Retension 
- specific period can be specified  for retention
- during that time blob can be read only after creation. 
- after that blob can be deleted but **Cannot be Updated**

## Legal Hold policy [more info](https://learn.microsoft.com/en-us/training/modules/storage-security/7-blob-data-retention-policies#:~:text=Legal%20hold%20policy%20support)

- if the retention time is not known *legal Hold policy* can be created.

## Life cycle managemnet policy
a policy can be made to automatically move blob from *hot* to *cool* and after that to *archive*.

## Object Replication in Blob [more info](https://learn.microsoft.com/en-us/training/modules/configure-blob-storage/6-determine-blob-object-replication)
- copies the blobs in a container asynchronously to another destination.
- **requires** blob versioning to be enabled on both the accounts. 
- source and destination containers can be in hot and cool access tiers. 



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