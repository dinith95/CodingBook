## Dealing with Nuggets

### Nugget shell commands 

> list all nuggets folder locations - ```dotnet nuget locals all --list```

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

before consumption of the keyed registration the `WithAttributeFiltering()` should be added to the registration of the *class which has the Keyed Registration*.

``` c#
// the ReadyToProcessService constructor consumes the GeneralProcessor
// with the key filter general
builder.RegisterType<ReadyToProcessService>().As<IReadyToProcessService>().WithAttributeFiltering();
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

## HttpClient Library 

### Creating with IHttpClientFactory [more info](https://learn.microsoft.com/en-us/training/modules/implement-http-operations-asp-razor/2-explore-http-clients)

- used as a factory abstraction through which the `HttpClient` can be created.
- exposes the HtppClient as a dependency injection ready type 

> Basic Implementation

``` c#

builder.Services.AddHttpClient(); // this will register HTTPClient factory 

// consumption of HttpClentFactory 

// DI in the constructor
public  class SampleService(
    IHttpClientFactory httpClientFactory,
    ILogger<SampleService> logger)

// create http client in method 
public async Task GetResponse(){
    // create http client using the factory
     using HttpClient client = httpClientFactory.CreateClient(); 
}
```

> Named Implementation
 - mupltiple `HttpClient` can be configured to return based on the name. 
``` c#
// registration of the httpclient factory 
builder.Services.AddHttpClient("catFacts", httpClient =>
{
    httpClient.BaseAddress = new Uri("https://catfact.ninja");
    
    // headers that should be sent with each request can be added here
    httpClient.DefaultRequestHeaders.Add("api-key", "<api=key>");  
});

// consumption through the HttpClientFactory 

// DI in the contructor 
 public SampleService(IHttpClientFactory httpClientFactory)
 {
     _httpClientFactory = httpClientFactory;
 }

// create http client in method 
public async Task GetResponse(){
    // create http client using the factory
     var httpClient = _httpClientFactory.CreateClient("catFacts");
}
```

> Typed Implementation 

- the HttpClient can be configured for perticular service 
- when the `HttpClient` is called in perticular service the client configured with that service will be returned 

``` c#

// registration of the httpclient factory 
 builder.Services.AddHttpClient<CatFactsService>( 
     client => { client.BaseAddress = new Uri("https://catfact.ninja"); });

// consumption  of HttpClient directly 

// DI in the contructor 
 public CatFactsService(HttpClient httpClient)
 {
     _httpClient = httpClient;
 }


 public async Task GetResponse(){
    //  get the response from the HttpClient 
     var response = await _httpClient.GetAsync("https://catfact.ninja/fact");
}
```