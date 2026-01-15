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
- created as a  **Reference Type**
- new instances create on the **heap**
  
## Variable Passing  
- passed by value ( separate copy is created )
- since **string is immutable** original value is never modified

## String Builder 
- mutable version of the `string` 
- highly memory efficient in iterative string modifications as unless multiple instance has to be created. 