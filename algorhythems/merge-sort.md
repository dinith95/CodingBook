## into 

in merge sort the array is broken into indiviudals arrays and sorted like that . [mergesort-explanantion](https://www.youtube.com/watch?v=cVZMah9kEjI)

## sample steps 

 - deconstruct the existing until all the elements are in arrays of single element. 
 - merges the two individual element arrays 
 - continue merging until full array is creatd. 

 ## implementation 
 here in general following steps are follwed 

 - if array length is 1 or less return 
 - divide main array to two sub arrays by mid element
 - apply *Mergesort* for the both  the arrays individually and sort them recursively
 - merge two sorted arrays 

 ``` py
 def MergeSort(arr:list):
    if(len(arr) <= 1):
        return 

    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    ## deconstruct until all elements in arrays of one element 
    MergeSort(left_arr)
    MergeSort(right_arr)

    li = 0 # left array index
    ri = 0 # right array index
    mi = 0 # merged array index 

    ## initial merge with the arrays 
    while li < len(left_arr) and ri < len(right_arr):

        # compare first elements of left array with first element in right array 
        # if left array element is less , add that element to merged array
        if(left_arr[li] <= right_arr [ri]):
            arr[mi] = left_arr[li]
            li += 1

        # if right element is less add that to the merged array
        else :
            arr[mi] = right_arr[ri]
            ri += 1

        # increment the postion of the merged array
        mi += 1

    ## copy remaining  elemnets in left array
    while li < len(left_arr):
        arr[mi] = left_arr[li]
        li += 1
        mi += 1

    ## copy the remaining elements in right array
    while ri < len(right_arr):
        arr[mi] = right_arr[ri]
        ri += 1 
        mi += 1

```
  