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

or to get the name of the enum we can use the method `ToString()`. 

example : 

``` c#
// weekdays enums 
public enum WeekDays 
{ 
    Monday , Tuesday, Wednesday, Thursday, Friday
}

 string day = WeekDays.Monday.ToString() ; // return the "Monday" 
```

## Pattern Matching 

switch or nested if statements can be simplified using the above pattern matching statements . 

Ms learn link : [Learn Link](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/functional/pattern-matching#compare-discrete-values)


Notes to keep in mind : 
- the `_` means any value 
- make sure all combinations are covered 
- the matching order matters 

eg : SAmple pattern matching to Get grade 

``` C#
 private static string GetGrade(int marks)
 {
     return marks switch
     {
         > 75 => "A",
         > 65 => "B",
         > 55 => "C",
         > 40 => "S",
         _ => "F" 
     };
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

An iterator value can be also take with the select command 

``` c#
// here c - city <string> , i - iterator <int>
 var lines = cities.Select((c, i) => $"{i}. {c}").ToList();
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

### Zip 

used to iterate over 2 lists sequentially  and returns value returning from the lamda function

``` C# 
 int[] numbers = { 1, 2, 3 };
 string[] words = { "one", "two", "three" };
// iterate both numbers and words list items and retun the concat of the each element 
 var totals = numbers.Zip(words, (num, word) =>$"{num} => {word}");

  foreach (var e in totals)
  {
      Console.Out.WriteLine(e);
  }

// output 
// 1 => one
// 2 => two
// 3 => three
 
```

### Sort 

it sorts a list items default by **ascending order** . 

sort can be used with the **IComparer** to provide custom comparison

``` c# 

  var words = new List<string> {"falcon", "order", "war", "sky", "ocean", "blue", "cloud","boy", "by", "raven", "station", "batallion"};

  words.Sort((a, b) => a.Length.CompareTo(b.Length));  // sorts ascending length

  words.Sort((a, b) => b.Length.CompareTo(a.Length)); // sorts decending length

```

### Take while 
it will enumerate over a result set and return result until a given condition becomes false .

``` c#

int[] numbers = { 5, 4, 1, 3, 9, 8, 6, 7, 2, 0 };
var firstNumbers = numbers.TakeWhile(n => n < 6);
// output => 5, ,4 ,1 , 3

```
in the above code chunk it will excute until **9** on which the given conditon becomes false. 

## Exceptions 

### creating exceptions 

> adding custom data to an exception

``` C#
OperationCanceledException exception = new OperationCanceledException();
// adds custom data key => type , value => lightweight 
exception.Data.Add("type", "lightweight"); 

```




## Useful Methods 

### compare to 

compared the two objects and return an integer value base on the two values . 

sample 

``` c# 
obj1.val.CompareTo(obj2.val) ; // compare two object values 
 
val1.CompareTo(val2) ; // compare 2 values 

```

**results**

> 1st object < 2nd objct => < 0 

> 1st object  = 2nd object  =>  0 

> 1st object > 2nd object => > 0



