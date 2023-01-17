## Dealing with Nugets

### Nugget shell commands 

> list all nuggets folder loations - ```dotnet nuget locals all --list```

> clear all local nugget folder - ```dotnet nuget locals all --clear```



## Task Parallel Library 

### key points 
> Do not use .Result  unless the task has already completed the execution

> Do not use async void  user async Task 

> Do not use wait()  it can lead to deadlocks 
        ,

### creating new task 
A new task can be created from *Task.Run()* command . 

``` C#
Task task =  Task.Run(() => downLoadLogfile(outputfolder, Path.Join(azurePath, item.Name), item));
                // downLoadLogfile => async method which returns a Task 
```

also abive tasks can be added to a list as shown below and **can be held till all are completed**

``` C# 
 List<Task> downLoadTask = new List<Task>(); // creation of task list 

downLoadTask.Add(task); // adding to list 

Task.WaitAll(downLoadTask.ToArray()); // waiting until all of them are completed 
```


## Activator Library 

Activatior can be used to create a object on the runtime based on Reflection. 

the below code will create instance of **Type \<T> ** dynamically in run time .
Note that you pass the varaibels also to the construcotor class.  

``` c#

public static T GetService<T>(IConfiguration config)
{
    return (T)Activator.CreateInstance(typeof(T), new object[] { config });
}
```
