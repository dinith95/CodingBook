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