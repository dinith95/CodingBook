## Querying Date

When querying in the SQL date can be written in **YYYYMMDD** format.

> eg : 2023-08-25 can be written `'20230825'`

## NOT IN NULL Trap

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

## connecting to local db

refer the sql server [LocalDb doc](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver15)

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

the **Instance pipe name** is the connection string for the database.
