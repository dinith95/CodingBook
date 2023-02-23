# SQL Server on VM

VM instance with the SQL server installed on it. 

- IaaS approach 
- very much similar to SQL server running on premise server , only difference is that it is running on a VM in azure.
- suitable to migrate **on premise sql servers** which need **access to O/S feaatures**. 

# SQL Database Managed Instance 

runs a full instance of sql server on cloud . 

> managed by azure 

- backups 
- db replication
- instance resizing and config
- software patchng 
- db monitoring 

> managed by user 

- multiple daabases 
- security 
- resource allocation in between db

# Azure SQL DB 

Quick;y setup a database in the cloud , user manage only the data and the scaling of the database . 

## single db -  serverless 
database is in shared server with the dbs of the other azure clients 
 - scales automatially 
 - resources are allocated and removed when needed .

 ## elastic pool 
 - a resource pool should be created . 
 - the dbs created will share the resouces on the pool. 