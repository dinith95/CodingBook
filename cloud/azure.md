## common errors 

### could nt start storage emulator 

this is mostly due to the a **another software using port 10000**.
to resolve :
- find programme using port 10000 by - 
```powershell
netstat -p tcp -ano | findstr :10000
```

- run **terminal** in **admin mode** and kill process 
```powershell
taskkill /PID < process-number > /F
```
  -for  more info refer   [kill a task](../scripting/powershell.md#kill-a-task) in powershell doc 



## Azure storage 

### download files from azure file share 

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

> **--exclude-pattern**  - removes specific file mathcing the path from the pattern from the download list 

eg => ``` --exclude-pattern="tree.json"```

### Get a list of files from Azure file share 

use the list command ``` .\azcopy.exe list <url><folder_path>?<sas_token> <destination> ```

>  *url* - url of the azure file or diectory 

> *folder_path* - folder path inside the file share 

> *sas_token* - the token created defining permissions 


**Note**

``` .\azcopy.exe list <url><folder_path>?<sas_token>  > result.txt ```

will print the output to a text file.
