# basic coding syntax
## functions

### slice 

An array or list can be sliced as it returns a subset of elemetns .
Example slicings : ****

```py
num_arr = [1,2,3,4,5,6]

print(num_arr[0]) # prints 0
print(num_arr[-1]) # prints 6
print(num_arr[1:3]) # prints [1, 2]
print(num_arr[:3]) # prints [0, 1, 2]
print(num_arr[2:]) # prints [2, 3, 4, 5, 6]

```

## string operations 

- in python strings are considered as arrays 
- following short codes can be used to get substrings 

```py
name = 'dinith'
print(name[0]) # prints 'd'
print(name[-1]) # prints 'h'
print(name[1:3]) # prints 'in'
print(name[:3]) # prints 'din'
print(name[2:]) # prints 'nith'
```

## Lists 

- store multiple values as an array 
- **ordered** 
- **mutable**
- **indexed** ( can have repeating values)

create a list - `lista = [1, 2, 3, 4, 5]`

all list methods - [methods](https://www.w3schools.com/python/python_lists_methods.asp)

### create list through Comprehension
 - short hand syntax for creating list based on condition

```py
list2 = [x for x in range(10) ]  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [x for x in range(10) if x % 2 == 0] # prints [0, 2, 4, 6, 8]
list4 = [x*2 for x in range(10)] # prints [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## tuple 

- stores multiple elements as an array 
- **ordered**
- **immutable**
- **indexed** ( can have repeated values )

create a tuple 
- `tuplea = (1, 2, 3, 4, 5)`
- `tupleb = tuple(tuplea)` 

tuple methods - [methods](https://www.w3schools.com/python/python_tuples_methods.asp)

### create a tuple through comprehension 
 - short hand notation to create a tuple 

```py
tuple1 = tuple(x for x in range(10)) # prints (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple2 = tuple(x for x in range(10) if x % 2 == 0) # prints (0, 2, 4, 6, 8)
tuple3 = tuple(x*2 for x in range(10)) # prints (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
```

## Set 
- store multiple elements 
- **unordered**
- **immutable** ( can add and remove items)
- **unindexed**

> creating a set 

```py 
seta = {1, 2, 3, 4, 5} # default method
setb = {x for x in range(10) if x % 2 == 0} # using comprehension to create a set of even numbers from 0 to 9
```

set methods - [method](https://www.w3schools.com/python/python_sets_methods.asp) 

### Diffrence 

- get the values in **set1**  but not in **set2** 
- **syntax** : `diff = set1.difference(set2)`
- **short syntax** : `diff2 = set1 - set2`

```py 
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3,10} 

diff = set1.difference(set2) # returns {4, 5}
```

### Intersection 
- prints the common elements in both sets 
- **syntax** : `result = set1.intersection(set2)`
- **short syntax** : `result2 = set1 & set2`

```py
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3,10} 

result = set1.intersection(set2) # return {1, 2, 3}
```

### IsSubset 
- returns **True** all the elements in *set2* are exists in *set1*
- **syntax** : `result = set2.issubset(set1)`
- **short syntax** : `result2 = set2 <= set1 `

```py
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3} 

result = set2.issubset(set1)  # returns True
```

### IsSuperset 
- returns **True** if **set1** has all the elements in **set2**
- **syntax** : `result = set1.issuperset(set2)`
- **short syntax**: `result2 = set1 >= set2`

```py
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3} 

result = set1.issuperset(set2)  # returns True
```

### Union 
- returns all the elements in both sets 
- if there are duplicates , *they are included once*
- **sytax** : `result = set1.union(set2)`
- **short syntax** : `result2 = set1 | set2`

```py
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3,6} 

result = set1.union(set2)  # returns {1, 2, 3, 4, 5, 6}
```

### symmetric_difference
- returns element that are unique to two sets 
- common elements are not returned at all 
- **syntax** : `result = set1.symmetric_difference(set2)`
- **short syntax** : `result2 = set1 ^ set2`

```py
set1 = {1, 2, 3, 4, 5} 
set2 = {1,2,3,6} 

result = set1.symmetric_difference(set2) # returns {4, 5, 6}
```

## multiple arguments

In python method overloading is not required as it will modify the function as of the presesnted arguments .
But the **default values should be assigned** , if not it will return an error.

``` py
def myInfo(name='dinith' , age  = 20):
   print(name + ' age is ' ,age )

myInfo(); # works without any params
   # output -- dinith age is  **20**

myInfo(age=36, name='dj') # order of the parameter can be changed
   # output -- dj age is  36

myInfo(name = 'dj')   # can paas only some parameters , still the function works
   # output -- dj age is  20
```

Also functions can be defined such that it takes infinite arguments .

``` py
def addNos(*args):
   total = 0
   for a in args:
       total += a
   print(total)

addNos(2,3) 
   ## output ## - 5

addNos(2,5,8)
   ## output ## - 15

addNos(1,2,3,4,5,6,7,8,9)
   ## output ## - 45
```

## python file handling

file can be open and contents can be written to python in relative ease

file handling modes

- r - read only
- w - write
- a - appened

**Note** - all the files opened should be closed .

``` py
# open command take 2 arguments  , file path and the mode
file1 = open(os.path.join(path,'sample.txt'),'a') 
text = file1.read() ## read the everything on file 1 to text varaible
line1 = file.readline() ## read the first line of the file

# here the file is read line by line without storing data to memory
for row in file1:
    vals = row.split(',')

# writing to a file 
sampleStr = 'i am dinith'
file1.write(sampleStr)
file1.close()
```

# modules and classes
## python modules mangement 

python modules are a library in python . there are 2 ways to concume module in python .

### importing as module 
here the whole module is imported . 

```py
import random # random libaray is imported as module
print(random.randint(1,10))
```

### importing a specif function only 
here the specific function of the module is imprted to the namespace . 
> warn - if you have exsiting implementation with same name in module . this will casue erros.

```py
from random import randint 
#  ranint function is imported from the random library

print(randint(1, 10))
```

### guarding main method.
The main method can be accidently called when the module is imported by another module. 
To prevent this below systax is used 

```py
if __name__ == "__main__":
   Main() ## main will be called only when file is excuted directly

```
if python modukle is executed directly the **\_\_name__** is set to the *"\_\_main__"*

executed through an import the **\_\_name__** is set to the *name of the module*



### import from another python file

a function can be called from another python file as shown below .

``` py
## import the get version function in the source.py file
from source import getVersion 

print(getVersion()) ## get version function is called 
```

**Note** - if the imported files reside in a folder name of that folder should added as shown below

``` py
## source file exist in testPath folder
from testPath.source import getVersion 
```


## python modules

Python has several useful modules which we could consume to write the scripts .

### OS module

use to do the OS tasks such as manipulating files and directories .

### subprocess modules

used to call the other bash or powershell scripts

## python classe

python classes has below syntax 

```py
class Student:
    
    # constructor 
    def __init__(self, name, age):
        self.name = name # calls the proerty setter method 
        self.age = age

    # declare the property of a class    
    @property
    def age(self):
        return self._age

    # property setter method : set the property of class 
    @age.setter
    def age(self,age):
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name
```





# Useful Libraries 

## sys libarary 
shows the values in the python runtime environment. 

> sys.argv returns a list of arguments passed when calling the python file. 

```py 
import sys
## prints the name when python script is called . 
## here 1 is used as 0 has the name of the python file which is executed. 
print('hello: ' + sys.argv[1])
```

# python data structures 

## tuples 
- similar to a list 
- but are immtable 

```py
def getNums():
    ## this returns a tuple of 2 random numbers
    return (randint(1, 10),randint(11, 20))

## consuming the tuple 
t = getNums() 
print(f'num 1: {t[0]} \nnum 2 : {t[1]}') 
```

# python unit tests

python has support for the unit tests .

most of the unit test has following format . 

> logic module  - this has the functional logic: **calc.py**
```py
def sum(a,b):
    return a + b
```

> test librarry - this has tooling and support for python test : **pytest**.

> uni test module - unit tests the functions in logic module: **calc_test.py**

```py
def test_sum123():
    assert sum(1,3) == 4
    assert sum(0,4) == 4
```

# python useful packages 

## structlink
[struct link docs](https://eeshannarula29.github.io/structlinks/) - this implements linked list , trees , graphs and hash maps

