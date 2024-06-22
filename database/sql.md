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

## Data Types 

### Char(n)
- declared as `CHAR(50)`
- storeas fixed length of characters 
- if a s string with lesser number of chars added sql server automatically add blank spaces. 

### NChar(n)
- declared as `NCHAR(50)`
- similar to *char* but can store *unicode* characters. 

### Varchar(n)
- declared as `VARCHAR(50)`
- variable length characters can be stored
- n specifies the number of characters 

### NVarchar(n)
- declared as `NVARCHAR(50)`
- can store variable length of characters 
- can store the non unicode charactor data 

### Bit 
- declared as `BIT` 
- can store 0 or 1 or NULL 
- used to represent Boolean Data 

### Decimal ( Numeric )

- declared as `DECIMAL(8,5)`
- total of 8 chars
- 5 chars after the decimal point
- so the max value `999.99999`

### Float 
- approximate number datatype , the numbers here are of approximate values 
-  should never be used for finance , accounting information


### Unique Identifier
- hexadecimal number which is globally unique 
- can be generated through the `NEWID()` function 
- can set th table creation the value to `DEFAULT` to `NEWID()`
    example :
``` sql
    CREATE TABLE [hcm].[departments2]
    (
        dept_id UNIQUEIDENTIFIER DEFAULT NEWID(),
        dept_name VARCHAR(30)
    )
```

- can be also generated through the `NEWSEQUENTIALID()` , this generate sequential id which have few properties 
    - faster than `newid(0)` 
    - works better in the indexing 
    - **next created id can be guessed**

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

## sample Stored procedure 

set of SQL statements which can be executed. 

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

>[!NOTE]
**SET NOCOUNT ON;** - stop the update messages sent by SSMS \
**SET XACT_ABORT ON;** - rollback the updates in any error condition

stored procedure with out parameter 
```sql
CREATE PROCEDURE [dbo].AddNewPark
(
    @park_name VARCHAR(50),
    @entry_fee DECIMAL(6,2),
    @park_id INT OUT -- this parameter is returned and OUT should be present
)
AS 

SET NOCOUNT ON; -- stop sending the no of rows updated messages 
SET XACT_ABORT ON; -- rollback the stored procedure in any error condition

BEGIN 
    INSERT INTO [dbo].parks2 (park_name,entry_fee)
    VALUES (@park_name , @entry_fee);

SET @park_id = SCOPE_IDENTITY(); -- return the added row id 
END

GO

-- calling the stored procedure 
DECLARE @parkId INT; -- variable to get return value 

EXEC [dbo].AddNewPark @park_name = 'Green Meadows', @entry_fee = 5,  @park_id = @parkId OUT; -- OUT should be specified unless the return value will not be captured 
SELECT @parkId;
```

## Scaler Functions

### CONCAT Function 

- combine two or more string values together. 
- *NULL* values will be automatically replaced by *empty strings* in the concat function. 
- the below query will *CONCAT*  the firstName and the lastName as **FullNaame**. 

```SQL
SELECT c.customer_id , CONCAT(c.first_name,' ',c.last_name) as FullName 
FROM oes.customers c
```

### CHARINDEX Function

- get the positon of perticular character ( starting pos: 1 )
- syntax ```CHARINDEX( <char>, <string>)```
- the below query shows the postion of *@* symbol in each email address 

```SQL
SELECT c.email , CHARINDEX('@', c.email) As Atpos
FROM oes.customers c
```

### SUBSTRING Function

- returns defined number of characters from defined starting position of a string
- it *includes the character* at the *starting pos* 
- syntax: `SUBSTRING( <string>, <start pos>, <number of chars> )`
- below query returns 6 characters left of 4th character ( including 4th character.)

```SQL
SELECT c.email , SUBSTRING(c.email, 4, 6) As substr
FROM oes.customers c
```

### GETDATE Function

- get the current date and time as per location of SQL server on  which the query is run 
- sample 

```SQL 
SELECT GETDATE(); -- returns 2023-09-19 02:58:38.893
```

### CURRENT_TIMESTAMP

- get the current date and time as per location of SQL server which the query is run as similar to GETDATE()

```SQL
SELECT   CURRENT_TIMESTAMP  -- returns 2023-09-19 02:58:38.893
```

###  SYSDATETIME()

- get the current date and time as per location of SQL server which the query is run as similar to GETDATE() 
- but it **much more precise**

```SQL
SELECT  SYSDATETIME() -- 2023-09-19 02:58:38.8951834
```

### GETUTCDATE()
- get the current date time in **UTC  format** . 
- sample 

```SQL
SELECT GETUTCDATE() as UtcDate -- 2023-09-24 14:22:26.353
```

### DATEPART() 
- get the portion of DAY | MONTH | YEAR  in a date . 
- ex: if we specify month it will return the month number of a perticular date

```SQL
SELECT DATEPART( MONTH, GETDATE()) as 'month' -- 9
```

### DATENAME()

- return the portion of the date as a string 
- even year and day will be return as a string 

```SQL
SELECT DATENAME(MONTH, GETDATE()) as 'month' -- September
SELECT DATENAME(DAY, GETDATE()) as 'day' -- 29 
```

### DATEDIFF()
- return the difference between 2 dates in specified portion 
- difference between date1 and date2 will be given in **days**. 

```SQL
SELECT DATEDIFF(DAY, DATEADD(DAY,-5,GETDATE()) , GETDATE()) AS 'daysDiff' -- 5 
```

### SCOPE_IDENTITY()
- returns the last value inserted to the Identity column in a table

## window Functions 

operate on multiple rows at a time and return one output per row 

### RANK Function 

thiss functions assigns a rank to each of the items in the table after partitioning the result set . 

- PARTITION BY - partition the result set based on criteria ( eg: employees dataset by deprtment )

- ORDER BY - orders the results set in the partition by a criteria . ( Eg: employees within the department by the salary )

syntax 
```SQL
RANK() OVER (PARTITION BY <expr> ORDER BY <expr> [ ASC | DESC ] )
```


## Set operators 

- when 2 nulls are compared they are evaluated to TRUE. 
- colum numbers returned from each select statement  should be same 
- column's data types should match
- the column names of the first table will be displayed.  

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


## contraints 

### Unique Contraints 

- ensures all the values are unique 
- if multiple rows specified combinations should be unique. 
- does allow a single null value not multiple null values 
- table can have **multiple unique constrainsts**.

### Chek Constraints 

- applied to a column to check value in that column meets a condition 
- check constraint **allows nulls** to be inserted to the column. 


## sample SQL Statements 

## DML Statements 

### DISTINCT  statement

To remove the duplicates from the result set. 

If multiple values are there **duplicates of combinations** of those values will be removed

### DELETE &  TRUNCATE  statements 
 - Both the statemnets are used to remove the records 
 - Bith of these statments **can be rolled back** if it is within a Trasaction. 

| Delete Statemnt | Truncate Statement |
|-----------------|---------------------|
| `WHERE` clause can be specified| no `WHEREE` clause |
| enters records into `Transaction` log ( slower)| use optimised logging ( more faster)| 
| does not reset the coloumn identity  | reset identity to seed value | 
| Can be used with table has `FK`, | cannot use with table having `FK`

- **Note**
    - in `DELETE` auto increment id will note be reset to seed value, i.e when new record is added id will start at the next value not the seed value 
    - in `TRUNCATE`  the auto increment id is set to seed value. 
    - in `DELETE` there should not be related rows in child table 
    - in `tRUNCATE` the forign-key should be dropped and recreated. 
 
### DROP TABLE  

- remove **all the data and table structure**. 
- if there is `FK` the FK should be dropped and recreated. 

### ALTER COLUMN
- change the coloumns data type 
- can used to add `NOT NULL` ( before this is run coloumn should not have rows with null values)

### DROP COLUMN
- remove a column from the table 
- the column will be removed with its data also. 

### Rename Column 
- should run the built it stored procedure `sp_rename`.

```SQL
    sp_rename 'dbo.product.product_name', 'prod_name', 'COLUMN'
```

## Data Query Statements 

### ORDER BY  

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

### TOP 

return top most n records filtered for the result set . 

``` SQL
-- select employee with least salary
SELECT top 1 WITH TIES  emp.first_name, emp.last_name
FROM hcm.employees emp
ORDER BY emp.salary 
```

**WITH TIES** - this will send all the tied records for a perticular position. 

### GROUP BY 

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

###  HAVING 

HAVING CLAUSE  *filters the results of the GROUP BY*  based on a condition.

``` SQL
-- the customer data which is grouped by the state-province 
-- is filtered groups which has more than 4 records 
SELECT c.state_province , COUNT(c.customer_id)
FROM oes.customers c
GROUP BY c.state_province
HAVING COUNT(c.customer_id) > 4
```
### IN
- IN operator allows WHERE  clause to compare  on multiple values ( i.e , similar to multiple OR statements )
- in the below query it will return values for products with prices **20 or 30 or 40**

```SQL
SELECT p.product_id, p.product_name, p.list_price, p.category_id 
FROM oes.products p
WHERE p.list_price IN ( 20, 30 ,40 )
```

- IN can be  used with a subquery,  

```SQL
SELECT p.product_id, p.product_name, p.list_price, p.category_id 
FROM oes.products p
WHERE p.list_price IN ( 
    SELECT MIN(p2.list_price)  FROM oes.products p2
    )
```
in the above query info is returned only for products which has minimum proce ( satisfies the sub query).

### NOT IN 
- NOT IN  operator returns the values for which the value in question in not within the specified set. 
- in the below query it will return values for products with prices except **20 or 30 or 40**.

```SQL
SELECT p.product_id, p.product_name, p.list_price, p.category_id 
FROM oes.products p
WHERE p.list_price NOT IN ( 20, 30 ,40 )
```

### EXISTS 

the exists returns **TRUE** if there are **one or more rows in subquery**. 

Note - exists is faster when the subquery result is large . 

### CASE Expressions 
- Use to define conditional value return.
- case statement should have **END**  clause 
- the name for the result column can be given after the **END** clause.  

> simple format 
```SQL
SELECT 
    p.product_id , p.product_name , p.discontinued, 
    CASE p.discontinued -- value on which logic is based on 
        WHEN  1 THEN 'YES' 
        WHEN  0 THEN 'NO'
        ELSE 'UNKNOWN'
    END AS disDescription
FROM oes.products p;
```

> normal format 

```SQL
SELECT 
    p.product_id , p.product_name, p.list_price,
    CASE 
        WHEN p.list_price < 50 THEN  'Low' -- conditinal statements 
        WHEN p.list_price >= 50 AND p.list_price  < 250 THEN 'Medium'
        WHEN  p.list_price >= 250 THEN 'High'
        ELSE 'Unknown'
    END AS 'PriceGrade'
FROM oes.products p 
```
### JSON_VALUE

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
### JSON_QUERY

used to extract a object or array of json data. 

format - `JSON_QUERY (jsonData , [Path Mode] JSON_path)`

``` SQL
-- return the data of the first empoyee in json data as result
SELECT  JSON_QUERY(@data, '$.employees[0]') AS 'Result';
```

### Common Table Expressions ( CTE )

> syntax of CTE 

```SQL
WITH <table_name> AS 
    ( 
        <sub query>
    ) 
<outer-query>
```
sample :
```SQL
-- the result set from the products table is taken as S
WITH s AS 
(
    SELECT p.product_id , p.product_name, p.list_price, p.category_id,
            RANK() OVER ( PARTITION BY p.category_id ORDER BY  p.list_price ASC) as rnk
        FROM oes.products p
)
-- the result set S is filtered as a normal query
SELECT s.product_id, s.product_name , s.list_price , s.category_id
FROM s 
WHERE S.rnk = 1

```
## concepts

### Concept of excution order

- the SQL engine **does not need to follw** the below order . 
- but it should return a *result as it has followed the below order*. 
[ms learn article](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=sql-server-ver16&redirectedfrom=MSDN#logical-processing-order-of-the-select-statement)

1. FROM 
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT 
6. DISTINCT
7. ORDER BY
8. TOP

### Concept of NULL 
In SQL NULL means the value is unknown . 

- Null will *never be equal to another null*
- *NULL* plus anything will return *NULL*

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



## Quick Tips

### Querying Date
When querying in the SQL  date can be written in **YYYYMMDD**  format. 

> eg : 2023-08-25 can be written `'20230825'`

### NOT IN NULL Trap 

if you are doing an SQL with a syntax similar to following ,

```SQL
SELECT <expression >
FROM <table> t
WHERE e.employee_id NOT IN (
    -- SUBQUERY 
    SELECT DISTINCT o.employee_id
    FROM oes.orders o
    WHERE o.employee_id IS NOT NULL
)
```

make sure that **sube query does not return any element as NULL**, if it does the final result will not return any results. 

it is advisable to add **IS NOT NULL** check as shown above. 

