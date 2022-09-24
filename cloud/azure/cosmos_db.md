Azure Cosmos Db is the noSQL database in which the values are stored as Key value pairs . 


# Reading Values - SQL API 

The values are queried through the **SQL API**. It provides an inbuilt tool to read and extract the values.


``` SQL
SELECT * FROM RetriggerScheduler c where ....

```

## User Defined Functions 
UDF is a javascript function which will support to filter and present cosmos db data in more filtered or processed manner . 

sample Udf function 

``` js
function userDefinedFunction(cubeReleases , compareDate){
   // funtion logic 

  return publishdate > cmpDate; // returns a bool 
}

// also we can return a value / object  as well
function userDefinedFunction(cubeReleases,spcode){
   // function logic

  return {
    sp : spcode,
    date : date,
    ficVer: fv
  }
}
```

UDF functions can be called in two ways 

> in the where clause ( these would return a bool mostly )

``` sql 
    SELECT f.id, f.address.city
    FROM f
    WHERE udf.userDefinedFunction(f.address, "2022-09-24")
```
> in the select cluase ( these would return a value )

``` sql
SELECT udf.userDefinedFunction(f.address, "2022-09-24")
FROM Families
```

## InBuilt Functions 

### Count 

return count of the attributes . 

``` SQL
SELECT count(c.Code) FROM rs c where c.ScheduleId = "50cdbbd3-5813-4300-b775-ada8105622e8"
```

### Order by 

will order the resutls by specific attribute value. 

``` SQL
SELECT  * FROM rs c where c.EntityName = "Schedule" order by c.StartTime  desc 

```
### Top

get specified top results of a collection .

``` SQL
SELECT Top 5 * FROM RetriggerScheduler c where c.EntityName = "Schedule"
```

this will return the top 5 results. 

### Array_Contains

filter by the items in an array . 

``` SQL
select * FROM RetriggerScheduler c 
 where 
   ARRAY_CONTAINS( [ "abc" , "def" , "ghi"] ,c.Code ) 

```

this will return the all the elements which would have *abc* *def* or *ghi* for the *Code* . 

### Array_Slice 

returns a specified portion of the array 

> syntax  ``` ARRAY_SLICE (<array>, <array position> , <items count>) ```

1.  array 

any array 

2. array position 

starting position of the array 

eg : 
  - 0 - first element 
  - 1 - second element
  - -1 - last element 
  - -2 - second last element 

3. items count 
  the number of items to be returned from the specified position. 

  eg : 
  ``` sql
  -- get last 10 elements 
  ARRAY_SLICE(c.History, -10 , 10) 
  ```

## system generated values 

### _ts value

The _ts property shows the *date and time* which the document was *last updated* . 

it is in [epoch](https://en.wikipedia.org/wiki/Unix_time) time . 

this can be taken to human readable time by calling function ``` TimestampToDateTime(c._ts*1000) ```

eg : 

``` sql 
SELECT c.FirstName , TimestampToDateTime(c._ts*1000) AS 'time' FROM Person c
```