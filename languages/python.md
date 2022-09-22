## python functions

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

### sys module 
use to manipulate the different parts of the python runtime env. 

### OS module

use to do the OS tasks such as manipulating files and directories . 

### subprocess modules 

used to call the other bash or powershell scripts 

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
sampleStr = 'i am dinith'
file1.write(sampleStr)
file1.close()
```


