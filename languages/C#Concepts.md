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
