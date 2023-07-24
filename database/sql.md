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
