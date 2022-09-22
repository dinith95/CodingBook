## python general patters

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

**Note** - all the files opened should be closed . 

``` py
# open command take 2 arguments  , file path and the mode
file1 = open(os.path.join(path,'sample.txt'),'a') 
sampleStr = 'i am dinith'
file1.write(sampleStr)
file1.close()
```


