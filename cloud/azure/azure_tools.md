# az copy tool

az copy tool download link : https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10

use the azcopy command ``` .\azcopy.exe copy <url><folder_path>?<sas_token> <destination> ```
main paratmeters 
>  *url* - url of the azure file or diectory 

> *folder_path* - folder path inside the file share 

> *sas_token* - the token created defining permissions 

> *destination* - the location of the local machine which the file will be copied . 

**other parameters**
> **--recursive** - download contents inside the directory 

> **--include-pattern**  - add a specific file pattern to download 

eg =>  ```--include-pattern="*.json"```

to add multiple files to download specify them by semi-colon - **:**

eg =>  ```--include-pattern="result_.xml;delivered;"```

> **--exclude-pattern**  - removes specific file mathcing the path from the pattern from the download list 

eg => ``` --exclude-pattern="tree.json"```

### Get a list of files from Azure file share 

use the list command ``` .\azcopy.exe list <url><folder_path>?<sas_token> <destination> ```

>  *url* - url of the azure file or diectory 

> *folder_path* - folder path inside the file share 

> *sas_token* - the token created defining permissions 


**Note**

``` .\azcopy.exe list <url><folder_path>?<sas_token>  > result.txt ```



sample command 
```powershell
 copy "<URL_OF_FILE>?<SAS_URL>" "D:\tempData\crawled-logs" --recursive --check-length=false --include-pattern="*.json" --exclude-pattern="tree.json"
 ```

### get list of files in a folder ### 

use the ```.\azcopy.exe list  <url>?<sas_token> ```. 

**Note** if you want to print to a textfile redirect the output to a text . 

sample 
```powershell 
.\azcopy.exe list "<URL_OF_FOLDER>?<SAS_TOKEN>" > result.txt
```
=======
will print the output to a text file.

### azcopy optimising the performance
The performance can be optimised by increasing the following varaibles 
- AZCOPY_CONCURRENT_FILES 
- AZCOPY_CONCURRENCY_VALUE ( No of concurrency HTTP connection )

to set an env varaible in powershell 
```powershell
$env:AZCOPY_CONCURRENCY_VALUE = <value>
```

# azure service bus explorer 
fre and opesource github tool [git repo](https://github.com/paolosalvatori/ServiceBusExplorer). 
can dowload the latest version from here : [releases](https://github.com/paolosalvatori/ServiceBusExplorer/releases)