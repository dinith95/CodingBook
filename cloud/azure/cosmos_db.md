Azure Cosmos Db is the noSQL database in which the values are stored as Key value pairs . 


# Reading Values - SQL API 

The values are queried through the **SQL API**. It provides an inbuilt tool to read and extract the values.


``` SQL
SELECT * FROM RetriggerScheduler c where ....

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


