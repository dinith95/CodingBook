## Introduction

linked list is set of elements are linked to eachother by uisng the pointers. 

![result](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)

[image credit : https://www.geeksforgeeks.org/]. 

linked list **node** can be represented as below. 

``` python
class Node:
  
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None
```

## operations of linked list 

### Traversing a Licked list 

``` python
def TraverseLinkedList(list1: ListNode):
    items = []
    while list1:
        items.append(list1.val)
        list1 = list1.next

    return items
```

### Generate LinkedList 

> Generating as **starting value is last** element. 

``` python
def GenerateLinkedList(arrItems): 
    head = None

    for item in arrItems:
        if (head is None):
            head = ListNode(item)
            continue

        newNode = ListNode(item)
        newNode.next = head
        head = newNode

    return head
```
> Generating as **Starting value is first** element.

``` python
def GenerateToLinkedList2(arrItems):  # starting value is the top value
    head: ListNode = None
    rootNode: ListNode = None

    for item in arrItems:
        newNode = ListNode(item)

        if (head):
            head.next = newNode
            head = head.next

        else:
            head = newNode
            rootNode = newNode
    return rootNode
```

## insert item at beginnig 

> time complexity : **O(1)**

``` python
def AddElementAtBegining(list1: ListNode,  element):
    newNode = ListNode(element)
    newNode.next = list1
    return newNode
```
