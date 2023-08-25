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

## concepts

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

## Qick Tips

### Querying Date
When querying in the SQL  date can be written in **YYYYMMDD**  format. 

> eg : 2023-08-25 can be written '`20230825`'