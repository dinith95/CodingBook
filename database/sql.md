## connecting to local db 

refer the sql server  [LocalDb doc](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver15)

- create local db - `SqlLocalDB create TestInstance`
- start local db - `SqlLocalDB s TestInstance` 
- info local db - `SqlLocalDB i TestInstance` 
- get all instances in local db - `SqlLocalDB.exe i`

**note** - the info will provide info as below 

    Name:               TestInstance
    Version:            15.0.2000.5
    Shared name:
    Owner:              DESKTOP-NCJ144J\Dinith
    Auto-create:        No
    State:              Running
    Last start time:    7/10/2021 6:55:13 AM
    Instance pipe name: np:\\.\pipe\LOCALDB#7901EE7E\tsql\query

the **Instance pipe name**  is the connection string for the database.


## sample trigger 

sample code for the sql trigger 

``` sql
 CREATE TRIGGER TR_ADD_PAYMENT ON Payment
AFTER INSERT 
NOT FOR REPLICATION 
AS
 
BEGIN
    update Payment
    set  PaymentDate = GetDate()
    where PaymentId in ( select PaymentId from INSERTED)
END 
```

## sample procedure 

sample code for the stored procedure 
``` sql 
-- a parameter Amount is passed 
CREATE PROCEDURE PaymentsAbove @Amount int
AS
BEGIN
      select * from Payment where Amount  > @Amount
END;
 
--  calling the stored procedure
EXEC PaymentsAbove @Amount = 10
```

## Set operators 

- when 2 nulls are compared they are evaluated to TRUE. 
- coloums numbers returned from each select statement  should be same 
- coloumns data types should match
- the coloumn names of the first table will be displayed.  

### Set operator precedence 
1. INTERSECT 
2. UNION / UNION ALL / EXCEPT

### UNION 
- combines the output of 2 or more SELECT  statements. 
- UNION will remove the duplicate records. 

``` SQL 
SELECT cs.scientific_name FROM bird.california_sightings cs
UNION
SELECT ars.scientific_name FROM bird.arizona_sightings ars
```

> in the above the **scientific_name** records  from **california_sightings** are combined with the **arizona_sightings**. 

### INTERSECT  
they get the common set of records from two queries . 

``` SQL
SELECT c.customer_id 
     FROM oes.customers c 
INTERSECT
SELECT O.customer_id
      FROM oes.orders O
```

>  in the above example it get the *common customer ids* from the customer table and the orders table . 

### EXCEPT  
get the diffrence between the two select statements . 
here the *order of the select statments do matter*

``` SQL 
SELECT p.product_id 
    FROM oes.products p
EXCEPT
SELECT i.product_id
    FROM oes.inventories i
```

in the above example returns the products ids 
- in the **product table** 
- not in the **Inventories table**


## sample SQL Statements 

### DML Statements 

> DISTINCT  statement

To remove the duplicates from the result set. 

If multiple values are there **duplicates of combinations** of those values will be removed

### Data Query Statements 

> ORDER BY  

order the content by a coloumn in the table , default **Ascending**

``` SQL
-- order the results set by the population_count
SELECT   ap.species_id , ap.locality, ap.population_count
FROM bird.antarctic_populations ap
ORDER BY ap.population_count 

-- order the results set by the population_count
SELECT   ap.species_id , ap.locality, ap.population_count
FROM bird.antarctic_populations ap
ORDER BY 3 -- here 3 means the 3rd coloumn in the result set
```

> TOP 

return top most n records filtered for the result set . 

``` SQL
-- select employee with least salary
SELECT top 1 WITH TIES  emp.first_name, emp.last_name
FROM hcm.employees emp
ORDER BY emp.salary 
```

**WITH TIES** - this will send all the tied records for a perticular position. 

> GROUP BY 

this groups the data by the value in the given coloumn. 

Note that the **GROUP BY** clause will runs first before the **SELECT**  statements. 

``` SQL
-- customers data is groupd by the state_province coloumn
SELECT c.state_province , COUNT(c.customer_id)
FROM oes.customers c
GROUP BY c.state_province
```

In a sql statment with **GROUP BY**
- only coloumn which is in GROUP BY clause should exists in SELECT statment
- other coloumns should be in an *aggregate function*. 

>  HAVING 

HAVING CLAUSE  *filters the results of the GROUP BY*  based on a condition.

``` SQL
-- the customer data which is grouped by the state-province 
-- is filtered groups which has more than 4 records 
SELECT c.state_province , COUNT(c.customer_id)
FROM oes.customers c
GROUP BY c.state_province
HAVING COUNT(c.customer_id) > 4
```

> JSON_VALUE

format -  ``` JSON_VALUE (jsonData , [Path Mode] JSON_path)```

get a value of a JSON object stored as a string.

in a *SELECT CLAUSE* 
``` SQL
SELECT JSON_VALUE('{"name": "John", "age": 30}', '$.name') AS name -- return John as the result
 ```
in a *WHERE CLAUSE* 
``` SQL
-- returns all ids of SampleTable where section_id in JSON matches in the given value in data coloumn.
SELECT  t.Id
FROM SampleTable t
WHERE  JSON_VALUE(t.[Data] , '$.section_id') = '6488282009129ffba030ec5e'
```
> JSON_QUERY

used to extract a object or array of json data. 

format - `JSON_QUERY (jsonData , [Path Mode] JSON_path)`

``` SQL
-- return the data of the first empoyee in json data as result
SELECT  JSON_QUERY(@data, '$.employees[0]') AS 'Result';
```

## concepts

### Concept of excution order

- the SQL engine **does not need to follw** the below order . 
- but it should return a *result as it has followed the below order*. 

1. FROM 
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT 
6. ORDER BY

### Concept of NULL 
In SQL NULL means the value is unknown . 

Null will *never be equal to another null*

to check whther value is null - `IS NULL`

> ISNULL() function

this would check perticular value is null, 
    - *null* - replace with given value 
    - *not null* - return the value

``` SQL
-- checks whther bonus is null, if so replace it with 0
ISNULL(bonus,0) 
```

> COALESCE() function
returns the *first not null expression*

``` SQL
-- returns first of phone , mobile or work phone which has a value first 
-- if all the above are null return NA
COALESCE(emp.phone, emp.mobile, emp.workPhone, 'NA')
```

### Collations 

rules which define the way in which the *characters are compared*. 

Collations can be defined in the 
- server level 
- database level 
- coloumn level

sample collations : `Latin1_General_CI_AS` , here 
- CI -  case insensitive
- AS - Accent Sensitive ( a != á )

we can alther the collation in a query also 

```SQL
-- set colation to Case Sensitive  and Accent Sensitive
SELECT p.product_id, p.product_name 
FROM oes.products p
WHERE p.product_name = 'usb hub' 
COLLATE Latin1_General_CS_AS  
```

### Pattern Matching 

we can match diffrent character patterns using the pattern matching sytnx. 
We should use the **LIKE** keyword with any of the pattern matchings. 

sample pattern matching character 
- % =>  any number of characters 
- _ =>  single character
- [0-9] => any digit from  0 to 9 
- [A-Z] => any letter from A to Z 



## Qick Tips

### Querying Date
When querying in the SQL  date can be written in **YYYYMMDD**  format. 

> eg : 2023-08-25 can be written '`20230825`'