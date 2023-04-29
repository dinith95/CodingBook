## introduction 

this will  have 

> worse case scenario - O(n^2) 

    when the most of the array is sorted 

> average case scenario - O( n log(n) )
     
## implementation 

``` py
def partition(arr, left , right):
    i = left ## goes from left to right 
    j = right -1  ## goes from right to left 
    pivot = arr[right] # its common practise to select last element as pivot 
 
    while i < j:
        # i is looking for an element bigger than pivot element 
        while i < right and arr[i] < pivot:
            i += 1
        
        # j is looking for elelment less than pivot element
        while j > left and arr[j] > pivot:
            j -= 1

        # if i and j javent crossed swap the elements 
        if( i < j):
            arr[i] , arr[j] = arr[j], arr[i] 
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right] , arr[i]
    return i

def quickSort(arr, left , right):
    if(left >= right):
        return

    # get the correct positon of the pivot element 
    partion_pos = partition(arr,left,right)

    # apply quiksort recursively to the items from 0 to pivot elements in array
    quickSort(arr, left, partion_pos - 1) 

    # apply quicksort recursively to the items from piot element to end 
    quickSort(arr, partion_pos + 1, right)

```