
## file operations 


### unzip from memory 

- unzip and extract a file on the memory itself . 
- the unzipped content should not need to be stored in the disk . 

- also there isn't any nugets required.  
- [code sample](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-unzip-in-memory-cs)

### create and append a new zip file from 
- create a zip file and insert file into it 
- also add a file to an existing zip file
- [create zip](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-creatzip-cs)

- [append zip](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-c-snippets-appendzip-cs)

### Read and Write CSV data

this uses the nugget package [CSVHelper](https://www.nuget.org/packages/CsvHelper/). 

[Read from CSV file](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-read-from-csv-file-cs) - returns a *DataTable*

[Write to CSV File](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-write-to-csvfile-cs) - accepts a *DataTable*




## other operations 

### Create SHA1 hash 

- will generate the **SHA1 hash **  based on the given string
- [generate hash snippet](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-genhash-cs)

### generate dynamic class 
- create a dynamic class with the `ExpandoObject`
- [dynamic-class-creation-snippet](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-dynamic-class-cs)

## Generic Code smippets 

### Query cosmos Data 

A generic method can be created to query cosmos container data encapsulating the boiler plate logic. 

>[!info] Passing the Query string 

- paramsCollection - list of query params as a dicionary 

    eg : `var spQueryParams = new Dictionary<string, string>() { { "@docId", docId } };`

- container - the cosmosdb container 

- queryString - the sql like query string 

    eg : `SELECT c.StartPointCode, c.SagaStates FROM c where lower(c.DocumentId) = @docId`

- [query-code-snippet](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-cosmosquery_querystr-cs)

>[!info] passing the delegate 

- container - the cosmosdb container 

- filterFunction - delete function to do the data filtering 

    eg : `sp => sp.DocumentId.ToString().ToLower() == docId`

- selectFunc - it will project only the necessary propertese ( does the function of the select clause )

- [query-code-snippet](https://gist.github.com/dinith95/cddcdf4c32633b3abd182d7f57790e88#file-cosmosquery_delegate-cs)
