## .net sdk for storage 

### connect to storage from SAS 

connect to file storage through a SAS token. 

```c#
// pass sas token enclosed in Uri
var sc = new ShareClient(new Uri(config[sasKey]), null);
 var directory = sc.GetDirectoryClient("firectory1"); // path to the directory
```