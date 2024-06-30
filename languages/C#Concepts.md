## Abstract Class 
class is intended to be a `base class` for the other classes and `cannot be instanciated`. 

- abstract method should be implemented by the class which is derived from the abstract class. 
- abstract methods are `virtual` methods by default.
- `sealed` modifier cannot be applied with the abstract as they contradicts 

## Sealed Modifier
`sealed class` prevents the class from inheriting from it 
`sealed method` prevents a method being overridden. 

method override example 
```c#
class A
{
    public virtual void Method1() => Console.WriteLine("A.Method1");
}

class B : A
{
    // the method is sealed, so it cannot be overridden in a derived class
    public sealed override void Method1() => Console.WriteLine("B.Method1");
}

class C : B
{
    // Attempting to override B.Method1 causes a compile-time error
    public override void Method1() => Console.WriteLine("C.Method1");
}
```

## Constructors 

- uses to initialize the objects 
- it is called when the object is created 
- if there is no constructor defined compiler creates a **default constructor**
  - without any params 
  - if at least one constructor is defined the default is not created. 

### Constructor Overloading 

- as methods constructors also can be overloaded.
  
in constructor  ```this()``` can be called to call other overload constructors.

```c# 
 public class ClassA
{
    public ClassA()
    {
        Console.WriteLine("ClassA Constructor"); 
    }

    // when calling
    //  the constructor without any params will be called first  
    // next the constructor with params will be called
    public ClassA(string name):this()
    {
        Console.WriteLine("ClassA Constructor with name: " + name);
    }
}
```

> sample output 

```
ClassA Constructor
ClassA Constructor with name: Test
```

## Modifiers 

### Ref Modifier 
- use to pass a primitive data type as a reference. 

### Params Modifier 
- can pass multiple set of params which do not fix number of params . 
  
> example 

add varaible multiple numbers , like in one instance 2 numbers , another 3 numbers etc.
```c#
  // array of numbers is passed with params modifier
  private static int Add(params int[] numbers)
  {
      // logic to add numbers
      return 0;  
  }

  // above method can be called without init an array
    var v1 = Add(1, 3, 4); // add 3 numbers
  var v2 = Add(1, 2);// add 2 numbers
```
