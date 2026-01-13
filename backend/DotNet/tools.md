# CSharpier Code Formatting 
- link to tool [CSharpier](https://csharpier.com/docs/CLI)

## CLI Based Formatting 
- formats the code based on the CLI 

### Format command
 - `dotnet csharpier <directory>`
 - formats all the files in a directory given
 - Examples : 
  
```bash
dotnet csharpier . # format current folder 
dotnet csharpier .\ContentProcessingWorker # format the specified folder
```

### Check Command 
- `dotnet csharpier --check <directory>`
- check whether the code is formatted 
- Examples : 

```bash
dotnet csharpier --check . # check for the current directory
dotnet csharpier --check .\ContentProcessingWorker # check the specified folder
```