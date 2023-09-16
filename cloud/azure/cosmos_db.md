Azure Cosmos Db is the noSQL database in which the values are stored as Key value pairs .

> cosmos db version 
- key value 
- document 
- graph 
- coloumn family stores 

# Db Information

## Deployment plans

There are 2 deployment plans

- serverless 
- provisioned througpput
- autoscale 

### Serverless 

- consumption based model , user will be charged to each of the RUs used. 
- accounts only in one region
- max 50gb in container

### Autoscale
- set Max RUs amount can be specifed and the containers will scale within those values based on demand.
- minimum 10% of the max RUs count. 

## Throughputs 
number of RU tha can be consumed by an application in 1 second. 

when **Through is high** the db will **rate limit** or **throttle** the subcequent requests.

through can be specidied in multiple ways .

- database
- container
- combination of database and container

### Database level provisioning

- throughput values for complete database
- the containers under it will share the throughput

### container level 

- specified RU is only for the perticular container



# Reading Values - SQL API

The values are queried through the **SQL API**. It provides an inbuilt tool to read and extract the values.


``` SQL
SELECT * FROM RetriggerScheduler c where ....

```
## JOINS  
Joins can be used join the document on the same document and return an iterating set of element in the document as a collection. 

ex: think of a document structure like below and if there are multiple documents of the similar structure. 

```json
{
    "id": "2b161158aa25480ea6868ec4683cdcc6",
    // other json propertese  
    "Tags": [
        {
            "Label": "Citi-3",
            "id": "Citi-3"
        },
        {
            "Label": "Citi",
            "id": "Citi"
        },
        {
            "Label": "Monitored",
            "id": "Monitored"
        },
        {
            "Label": "ClassificationStandard",
            "id": "ClassificationStandard"
        }
    ]
}
```
if we need to get an enumeration for each of the tags with the id following query can be written . 

```sql
SELECT c.id, t.Label FROM c 
-- each document is joined on its tags 
join t in c.Tags
where c.id = '2b161158aa25480ea6868ec4683cdcc6'
```

the results set is 
```json 
[
    {
        "id": "2b161158aa25480ea6868ec4683cdcc6",
        "Label": "Citi-3"
    },
    {
        "id": "2b161158aa25480ea6868ec4683cdcc6",
        "Label": "Citi"
    },
    {
        "id": "2b161158aa25480ea6868ec4683cdcc6",
        "Label": "Monitored"
    },
    {
        "id": "2b161158aa25480ea6868ec4683cdcc6",
        "Label": "ClassificationStandard"
    }
]
```

> if you need to get filtered list of documents **with a property on tags** , you can use similar query as below. 

```SQL
SELECT c.id, t.Label FROM c 
join t in c.Tags
where t.Label = 'Citi'
```
this would returns info of **all documents with tag label citi**. 

```SQL
[
    {
        "id": "4ce342a1d78847e48a381b7e625bc9e3",
        "Label": "Citi"
    },
    {
        "id": "13a4648a55164e6db4887417f8caa4df",
        "Label": "Citi"
    },
    {
        "id": "bb5d5f7447d5478eba67ffb4d554a442",
        "Label": "Citi"
    },
    {
        "id": "0f468f69695040c1adf3b8bf06aa2baf",
        "Label": "Citi"
    }
]
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



# .net SDK with cosmos db

install the following nuget package 

``` Microsoft.Azure.Cosmos ```

## Creating the client connection 

```  c#
// create client connection 
var client = new CosmosClient(config["cosmos_connString"]); // pass connection string 

// get container 
// dbName - database name 
// container - name of the container
client.GetContainer(dbName,container);
```

## querting for values 

``` c#
// queryStr - query string 
var parameterizedQuery = new QueryDefinition(queryStr)
                                            .WithParameter("@id", regulator.Id);

// create the feed iterator and get the paged results 
using FeedIterator<Regulators> filteredFeed = container.GetItemQueryIterator<Regulators>(parameterizedQuery);


while (filteredFeed.HasMoreResults)
{
  // get the response dataset 
    FeedResponse<Regulators> response = await filteredFeed.ReadNextAsync();
    foreach (Regulators item in response)
      Console.WriteLine($"Found item:\t{item.name}");
        
              
}
```

> for more information regard to querying items refer [microsoft docs](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-dotnet-query-items#query-items-using-a-sql-query-asynchronously)


## Adding new element 

``` c#

// commonEntitites - the container name 
// type of item to be created
 await commonEntitites.CreateItemAsync<Regulators>(regData, new PartitionKey("Regulators"));

```

