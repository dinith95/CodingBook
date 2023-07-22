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

## Autofac Libary

Autofac is a Inversion of Control container library . It manages the dependencies with the classes so that applications can scale easily . 

### registering typical class 

``` c#
// initialise a container builder 
 ContainerBuilder builder = new ContainerBuilder();

 // class is registered with its interface 
  builder.RegisterType<FileService>().As<IFileService>();

// register as a instance object 
    builder.Register<ILogger>(c =>
            {
                return new LoggerConfiguration()
                .WriteTo.Console()
                .CreateLogger();
            })
            .SingleInstance();

// finally after registering all the types use build method to return container
    return builder.Build();
```

### consuming a typical class 

autofac will insert the constructor parameters. 
Only the relavant interface should be declared 

``` c#
public class MainService
{
    // declare the interface property 
     private readonly IFileService _fileService;

    // FileService object will be inserted by autofac
    public MainService(IFileService fileService)
    {
        _fileService = fileService;
    }
}

public void SampleMethod(){
    // or can be obtainer from the container object 
    var cubeService = container.Resolve<ICubeService>();
}


```

### keyed Registrations 

multiple implementations can be declred for the **same interface** as **keyed Registrations**. 

``` c#

// declaring the registrations 
     builder.RegisterType<GeneralProcessor>().Keyed<IProcessor>("general");
    builder.RegisterType<PipelineProcessor>().Keyed<IProcessor>("pipeline");

```

``` c#
// can be cosumed using container object 
     container.ResolveKeyed<IProcessor>("general");

// can be consumed through a key filter attribute in constructor
    public SampleConstructor([KeyFilter("general")]IProcessor processor)
    {
        _processor = processor;
    }
```