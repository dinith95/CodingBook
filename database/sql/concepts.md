## Concept of excution order

- the SQL engine **does not need to follw** the below order .
- but it should return a _result as it has followed the below order_.
  [ms learn article](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=sql-server-ver16&redirectedfrom=MSDN#logical-processing-order-of-the-select-statement)

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. TOP

## Concept of NULL

In SQL NULL means the value is unknown .

- Null will _never be equal to another null_
- _NULL_ plus anything will return _NULL_

to check whther value is null - `IS NULL`

> ISNULL() function

this would check perticular value is null, - _null_ - replace with given value - _not null_ - return the value

```SQL
-- checks whther bonus is null, if so replace it with 0
ISNULL(bonus,0)
```

> COALESCE() function
> returns the _first not null expression_

```SQL
-- returns first of phone , mobile or work phone which has a value first
-- if all the above are null return NA
COALESCE(emp.phone, emp.mobile, emp.workPhone, 'NA')
```

## Collations

rules which define the way in which the _characters are compared_.

Collations can be defined in the

- server level
- database level
- coloumn level

sample collations : `Latin1_General_CI_AS` , here

- CI - case insensitive
- AS - Accent Sensitive ( a != á )

we can alther the collation in a query also

```SQL
-- set colation to Case Sensitive  and Accent Sensitive
SELECT p.product_id, p.product_name
FROM oes.products p
WHERE p.product_name = 'usb hub'
COLLATE Latin1_General_CS_AS
```

## Pattern Matching

we can match diffrent character patterns using the pattern matching sytnx.
We should use the **LIKE** keyword with any of the pattern matchings.

sample pattern matching character

- % => any number of characters
- \_ => single character
- [0-9] => any digit from 0 to 9
- [A-Z] => any letter from A to Z

## Stored procedure

set of SQL statements which can be executed.

sample code [sample_sp](https://gist.github.com/dinith95/d9ded48a7a68673fd011414fcd1bfc0f)

> [!NOTE]
> **SET NOCOUNT ON;** - stop the update messages sent by SSMS \
> **SET XACT_ABORT ON;** - rollback the updates in any error condition

stored procedure with out parameter - [sp_out_param](https://gist.github.com/dinith95/d9ded48a7a68673fd011414fcd1bfc0f#file-sp_out_param-sql)

## Trigger

sample code for the sql trigger [sample_trigger](https://gist.github.com/dinith95/1c33068ac870bff4eea5b69b4590e488#file-simple_trigger-sql)
