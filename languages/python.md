# basic coding syntax
## functions

### slice 

An array or list can be sliced as it returns a subset of elemetns .

```py
import sys

nums = [1,2,3,4,5,6]

# here only 2nd to 4th elements are considered
# if ending position is not mentioned it will take until last element
for num in nums[1:3]:
    print(num)

```

## multiple arguments

In python method overloading is not required as it will modify the function as of the presesnted arguments .
But the **default values should be assigned** , if not it will return an error.

``` py
def myInfo(name='dinith' , age  = 20):
   print(name + ' age is ' ,age )

myInfo(); # works without any params
   # output -- dinith age is  20

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

