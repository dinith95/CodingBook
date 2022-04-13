## common commands 

### kill a task

use the command - ```taskkill /PID 12333 /F```
- *12333* - process number 
- */F* - forcefully kill a task 

### send a HTTP Request 

use the command ``` Invoke-RestMethod -Uri <uri> -Method <method>```

- *uri* - url that the request should be sent 
- *method* - HTTP method type , ( **GET/POST/PUT**)

> example 
```  powershell
Invoke-RestMethod -Uri https://reqbin.com/echo/post/json -Method POST
```

more information [microsoft documentation ](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod?view=powershell-7.1)

 


## powershell scripting 

### reading from the input prompt 

``` powershell
$response = Read-Host 'Please enter [y] to proceed or any other key to cancel'
```

### invoking a exe 

a exe file can be invoked with the exact path 
``` powershell 

$azCopyPath = 'D:\software\azcopy_tool\azcopy.exe'
& $azCopyPath rm <uri_with_sas>   --recursive=true

```

note : by adding the pipe to redirect to **Out-Host** the output can be redirected to console. 

``` powershell 
& $azCopyPath rm <uri_with_sas>   --recursive=true | Out-Host
```

###  function

> function should be declared with below pattern 

``` powershell
function DeleteDirectory {
    param (
        $dirs,
        $removingDirNames
    )
    # funtion logic
}
```

the above function can be called like below 

``` powershell 
DeleteDirectory -dirs $directories -removingDirNames $removingDirs
```

