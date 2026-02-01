## Data Types

### Char(n)

- declared as `CHAR(50)`
- storeas fixed length of characters
- if a s string with lesser number of chars added sql server automatically add blank spaces.

### NChar(n)

- declared as `NCHAR(50)`
- similar to _char_ but can store _unicode_ characters.

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
- should never be used for finance , accounting information

### Unique Identifier

- hexadecimal number which is globally unique
- can be generated through the `NEWID()` function
- can set th table creation the value to `DEFAULT` to `NEWID()`
  example :

```sql
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

````

## Set operators

- when 2 nulls are compared they are evaluated to TRUE.
- colum numbers returned from each select statement should be same
- column's data types should match
- the column names of the first table will be displayed.

### Set operator precedence

1. INTERSECT
2. UNION / UNION ALL / EXCEPT

### UNION

- combines the output of 2 or more SELECT statements.
- UNION will remove the duplicate records.

```SQL
SELECT cs.scientific_name FROM bird.california_sightings cs
UNION
SELECT ars.scientific_name FROM bird.arizona_sightings ars
````

> in the above the **scientific_name** records from **california_sightings** are combined with the **arizona_sightings**.

### INTERSECT

they get the common set of records from two queries .

```SQL
SELECT c.customer_id
     FROM oes.customers c
INTERSECT
SELECT O.customer_id
      FROM oes.orders O
```

> in the above example it get the _common customer ids_ from the customer table and the orders table .

### EXCEPT

get the diffrence between the two select statements .
here the _order of the select statments do matter_

```SQL
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

eg: check the department name is unique

```sql
ALTER TABLE [hcm].[departments]
ADD CONSTRAINT uk_departments_department_name UNIQUE (department_name)
```

### Check Constraints

- applied to a column to check value in that column meets a condition
- check constraint **allows nulls** to be inserted to the column.

eg: check salary is greator than 0 for all employees

```sql
ALTER TABLE [hcm].[employees]
ADD CONSTRAINT chk_employees_salary CHECK ([salary] > 0);
```

## sample SQL Statements

## DML Statements

### DISTINCT statement

To remove the duplicates from the result set.

If multiple values are there **duplicates of combinations** of those values will be removed

### DELETE & TRUNCATE statements

- Both the statemnets are used to remove the records
- Bith of these statments **can be rolled back** if it is within a Trasaction.

| Delete Statemnt                                 | Truncate Statement                   |
| ----------------------------------------------- | ------------------------------------ |
| `WHERE` clause can be specified                 | no `WHEREE` clause                   |
| enters records into `Transaction` log ( slower) | use optimised logging ( more faster) |
| does not reset the coloumn identity             | reset identity to seed value         |
| Can be used with table has `FK`,                | cannot use with table having `FK`    |

- **Note**
  - in `DELETE` auto increment id will note be reset to seed value, i.e when new record is added id will start at the next value not the seed value
  - in `TRUNCATE` the auto increment id is set to seed value.
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

```SQL
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

```SQL
-- select employee with least salary
SELECT top 1 WITH TIES  emp.first_name, emp.last_name
FROM hcm.employees emp
ORDER BY emp.salary
```

**WITH TIES** - this will send all the tied records for a perticular position.

### GROUP BY

this groups the data by the value in the given coloumn.

Note that the **GROUP BY** clause will runs first before the **SELECT** statements.

```SQL
-- customers data is groupd by the state_province coloumn
SELECT c.state_province , COUNT(c.customer_id)
FROM oes.customers c
GROUP BY c.state_province
```

In a sql statment with **GROUP BY**

- only coloumn which is in GROUP BY clause should exists in SELECT statment
- other coloumns should be in an _aggregate function_.

### HAVING

HAVING CLAUSE _filters the results of the GROUP BY_ based on a condition.

```SQL
-- the customer data which is grouped by the state-province
-- is filtered groups which has more than 4 records
SELECT c.state_province , COUNT(c.customer_id)
FROM oes.customers c
GROUP BY c.state_province
HAVING COUNT(c.customer_id) > 4
```

### IN

- IN operator allows WHERE clause to compare on multiple values ( i.e , similar to multiple OR statements )
- in the below query it will return values for products with prices **20 or 30 or 40**

```SQL
SELECT p.product_id, p.product_name, p.list_price, p.category_id
FROM oes.products p
WHERE p.list_price IN ( 20, 30 ,40 )
```

- IN can be used with a subquery,

```SQL
SELECT p.product_id, p.product_name, p.list_price, p.category_id
FROM oes.products p
WHERE p.list_price IN (
    SELECT MIN(p2.list_price)  FROM oes.products p2
    )
```

in the above query info is returned only for products which has minimum proce ( satisfies the sub query).

### NOT IN

- NOT IN operator returns the values for which the value in question in not within the specified set.
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
- case statement should have **END** clause
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

format - ` JSON_VALUE (jsonData , [Path Mode] JSON_path)`

get a value of a JSON object stored as a string.

in a _SELECT CLAUSE_

```SQL
SELECT JSON_VALUE('{"name": "John", "age": 30}', '$.name') AS name -- return John as the result
```

in a _WHERE CLAUSE_

```SQL
-- returns all ids of SampleTable where section_id in JSON matches in the given value in data coloumn.
SELECT  t.Id
FROM SampleTable t
WHERE  JSON_VALUE(t.[Data] , '$.section_id') = '6488282009129ffba030ec5e'
```

### JSON_QUERY

used to extract a object or array of json data.

format - `JSON_QUERY (jsonData , [Path Mode] JSON_path)`

```SQL
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
