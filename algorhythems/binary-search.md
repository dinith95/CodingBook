## into 

Binary search is used to search through an **ordered array** by divising the array into 2 parts in each time. 

## sample steps 

 - get the mid value of the array 
 - check with the value 
 - if its less use array partion from *arr[0]* to *arr[mid_val]* 
 else use array partion  *arr[mid_val]* to *arr[last]*
 - repeat above procedure 


## implementation 

``` py
def binary_search(input_array, value):
    arr_start = 0  ## defines starting element of trucated array
    arr_last = len(input_array) - 1 ## ending element of trucated array

## we need to get out an array with last 2 elements 
    while arr_start < arr_last - 1:
        midElement = (arr_last - arr_start) // 2
        midval = input_array[arr_start + midElement]

        if(midval == value):
            return arr_start + midElement
        if(value >= midval):
            arr_start += midElement
        else:
            arr_last -= midElement

    if input_array[arr_start] == value:
        return arr_start
    elif input_array[arr_last] == value:
        return arr_last
    else:
        return -1
```

