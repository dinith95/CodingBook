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