the big O notation shows how scalable the algorythem is . It basically tells how the algorhythem performs when list of inputs scale to few thousands or millions.

## 0(1)
> growth is constant irrespecting of data size 

 ```py
## nameslist - list of numbers 
def methodO1(numList):
    print(numList[0]) ## O(1)
```

this is because even how much bigger the parameters list the print line will be executed once. 

## O(n)
> growth is lenear respective to the input size

```py
## nameslist - list of numbers
def methodO2(numList):
    for num in numList:
        print(num) ## O(n)
```
 this because the number of print statements will vary according to the number number in array

 ## O(n^2)
> growth is expotential compared to the input size 

```py
## nameslist - list of numbers
def methOnPwr2(numList):
    for num1 in numList:
        for num2 in numList:
            print(f'combination : {num1},{num2}') ## O(n^2)
```

this is because based on the number of inputs the prints statements will vary expotetially
 - 10 inputs => 100 executions
 - 100 inputs => 10000 excutions

 ## O of multiple terms - O(a,b)
 > here multiple terms are given 

for function similar to below we can simplify to : `O(a+b)` 

```py
def print_items(a,b):
    for i in range(0,a):
        print(a)
    for j in range(0,b):
        print(b)
```