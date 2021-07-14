## string based enums 

string based enums can be created in C# in the following work around method 

``` C#
public static class RolesEnum
{
   public const string ADMIN = "Admin";
   public const string BUYER = "Buyer";
   public const string VISIOR = "Visitor";
}
```

## Linq queries 

Linq queries can be used to filter through arrays and list ( collections ) . Also very much handy in performing a quick operation to the lists. 

sample list - a list numbers is created with numbers from 1 to 100 as shown below 

``` C#
List<int> numbers = new List<int>();
 
List<int> numbersNew = new List<int>();
for (int i = 0; i < 100; i++)
{
    numbers.Add(i);
    numbersNew.Add(i + 100);
}
```

### Where 

it is used **select items based on condition** bu iterating a list . 
similar to the *filter* in js .

``` c#
// returns only numbers greater than 50 
 var list1 = numbers.Where(num => num > 50).ToList(); 
 ```

### Select 

it is used to iterate over items and return the each element **after modifying the element**. Similar to the *map* in js.

``` c#
// multiply every element by 2 and return values as a list 
var doubles = numbers.Select(num => num * 2).ToList();
```

### Any 
returns true if the **at least 1 element** satisfy the condition

``` c# 
// returns true if list has a single number greater than 50 
var greatorThan50 = numbers.Any(num => num > 50);
```

### All 
returns true if the **all elements** satisfy the condition.

``` C# 
// returns true if all the numbers are more than 50 
  var allGreatorThan50 = numbers.All(num => num > 50);

```

### Except 

returns the numbers in the first list but on in the second list 

``` c# 
 // returns all the elements in numbers list but not in the doubles list 
  var exceptItems = numbers.Except(doubles).ToList();
``` 

### Intersect 

returns all the items in **both the lists**.

``` C# 
var commonItems = numbers.Intersect(doubles).ToList();
```




        