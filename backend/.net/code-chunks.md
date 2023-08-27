
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
