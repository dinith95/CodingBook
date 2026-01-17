# Methods Handling

## Passing Variable number of Params

- C# allows to pass multiple amount of params given that they are **of the same type**.
- `params` should be given with **single Dimension Array**.
- only one params keyword per method.

```csharp
// definition
public int AddNumbers(params int[] numbers)
{
    return numbers.Sum();
}

// invoking
var total = sample.AddNumbers(1,2,3,4);
var total2 = sample.AddNumbers(1, 2);
```

# System.String & string

- `string` ( lowercase ) is just a reference to the `System.String` class
- `string` is used to follow the other variable types standard
- `String` is used when calling the static methods in the **system.String** class

## Immutable

- `string` is immutable if modified new instance is created

## Reference Type

- created as a **Reference Type**
- new instances create on the **heap**

## Variable Passing

- passed by value ( separate copy is created )
- since **string is immutable** original value is never modified

## String Builder

- mutable version of the `string`
- highly memory efficient in iterative string modifications as unless multiple instance has to be created.

# Streams

- read / write from / to source like file and network connection in sequential manner
- process data in chunk rather than reading everything at once
- buffered streams reduce the disk / network overhead by reading / writing in buffers
- use streams with **using statement** so that they are disposed properly

## Async Streams

- does not block the thread while wating till os / network to return data
- fewer threads are needed.
- allows server to handle multiple requests

# Threads and Async

- **Thread** : a single unit of code execution
- limited number of threads available in **thread pool**

## Behavior of Async

- when `await` keyword is hit , if method is not complete
  - a `Task` object is returned
  - `Thread` is returned to pool to take up another task
  - when the **Task is complete** a new htread is taken from pool and process is continued.
- this can be seen through following code

```csharp
 var thread = Thread.CurrentThread;
 Console.WriteLine($"SampleStreams running on thread {thread.ManagedThreadId}"); // returns an id
 await Task.Delay(3000);
 var thread2 = Thread.CurrentThread;
 Console.WriteLine($"SampleStreams resumed on thread {thread2.ManagedThreadId}"); // returns different id
```

## foreground vs background threads

- **foreground threads**

  - can set using `IsBackground=false`
  - keep the application running until they complete
  - default type of thread in .net

- **background threads**
  - can set using `IsBackground=true`
  - do not keep the application running ends when the foreground threads complete
  - used for tasks that run in background like monitoring file changes etc.
  - all threaads in thread pool are background threads unless specified by `IsBackground` property.
