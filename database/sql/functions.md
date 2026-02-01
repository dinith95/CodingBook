# Scaler Functions

## CONCAT Function

- combine two or more string values together.
- _NULL_ values will be automatically replaced by _empty strings_ in the concat function.
- the below query will _CONCAT_ the firstName and the lastName as **FullNaame**.

```SQL
SELECT c.customer_id , CONCAT(c.first_name,' ',c.last_name) as FullName
FROM oes.customers c
```

## CHARINDEX Function

- get the positon of perticular character ( starting pos: 1 )
- syntax `CHARINDEX( <char>, <string>)`
- the below query shows the postion of _@_ symbol in each email address

```SQL
SELECT c.email , CHARINDEX('@', c.email) As Atpos
FROM oes.customers c
```

## SUBSTRING Function

- returns defined number of characters from defined starting position of a string
- it _includes the character_ at the _starting pos_
- syntax: `SUBSTRING( <string>, <start pos>, <number of chars> )`
- below query returns 6 characters left of 4th character ( including 4th character.)

```SQL
SELECT c.email , SUBSTRING(c.email, 4, 6) As substr
FROM oes.customers c
```

## GETDATE Function

- get the current date and time as per location of SQL server on which the query is run
- sample

```SQL
SELECT GETDATE(); -- returns 2023-09-19 02:58:38.893
```

## CURRENT_TIMESTAMP

- get the current date and time as per location of SQL server which the query is run as similar to GETDATE()

```SQL
SELECT   CURRENT_TIMESTAMP  -- returns 2023-09-19 02:58:38.893
```

## SYSDATETIME()

- get the current date and time as per location of SQL server which the query is run as similar to GETDATE()
- but it **much more precise**

```SQL
SELECT  SYSDATETIME() -- 2023-09-19 02:58:38.8951834
```

## GETUTCDATE()

- get the current date time in **UTC format** .
- sample

```SQL
SELECT GETUTCDATE() as UtcDate -- 2023-09-24 14:22:26.353
```

## DATEPART()

- get the portion of DAY | MONTH | YEAR in a date .
- ex: if we specify month it will return the month number of a perticular date

```SQL
SELECT DATEPART( MONTH, GETDATE()) as 'month' -- 9
```

## DATENAME()

- return the portion of the date as a string
- even year and day will be return as a string

```SQL
SELECT DATENAME(MONTH, GETDATE()) as 'month' -- September
SELECT DATENAME(DAY, GETDATE()) as 'day' -- 29
```

## DATEDIFF()

- return the difference between 2 dates in specified portion
- difference between date1 and date2 will be given in **days**.

```SQL
SELECT DATEDIFF(DAY, DATEADD(DAY,-5,GETDATE()) , GETDATE()) AS 'daysDiff' -- 5
```

## SCOPE_IDENTITY()

- returns the last value inserted to the Identity column in a table

# window Functions

operate on multiple rows at a time and return one output per row

## RANK Function

thiss functions assigns a rank to each of the items in the table after partitioning the result set .

- PARTITION BY - partition the result set based on criteria ( eg: employees dataset by deprtment )

- ORDER BY - orders the results set in the partition by a criteria . ( Eg: employees within the department by the salary )

syntax

```SQL
RANK() OVER (PARTITION BY <expr> ORDER BY <expr> [ ASC | DESC ] )
```
