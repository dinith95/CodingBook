## Transactional Database

- used to process trasactions 
- both **read and write** optimised. 

### ACID semantics 
sample transaction => trasaction of cash is withdrawn bank account to cash account

> Atomacity - Each trasactions is a single unit of action

amount should be reduced from bank account and added to the cash account . Either both of them is recorded or none is recorded. 

> Consistancy - transactions should take data from one valid state to another. 

> Isolation - concurrent transactions cannot interfere with eachother. 

a application that reads bank balance cannot return information like this : 
Bank Balance => after trasaction occurred.
Cash Balance => before the trasaction occurred. 

> Durability - when trasaction is commited it will not change even if database system went offline.


## Analytical Databases

- ready heavy operations 
- store vast volumes of historical data 
- data is stored in data warehouses 

[more about analytical databases](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)

# SQL 

The stadered language to work with the database managment systems. 

## SQL statement typs 

### DDL statments 
create / modify / delete tables and records. 

eg : CREATE | DROP | ALTER

### DCL statemnts 

manage the accesss to the objects in the database .

eg: GRANT | DENY | REVOKE

### DML statements 

read and manipulate data 

eg: SELECT | INSERT | UPDATE 
