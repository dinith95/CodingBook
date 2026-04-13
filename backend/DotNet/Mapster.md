## Info 

- Mapping library in c# that is an ideal replacement for the **automapper**

## Mapster Code Generation tool 

### install mapper tool 

- use below command to install mapper tool 
  - `dotnet tool install Mapster.Tool`

### update csproj

- add following line to project csproj 
- these will automaitcally create the mapping classes in the csproj

```xml
<Target Name="Mapster" AfterTargets="AfterBuild">
  <Exec WorkingDirectory="$(ProjectDir)" Command="dotnet tool restore" />
  <Exec WorkingDirectory="$(ProjectDir)" Command="dotnet mapster model -a &quot;$(TargetDir)$(ProjectName).dll&quot;" />
  <Exec WorkingDirectory="$(ProjectDir)" Command="dotnet mapster extension -a &quot;$(TargetDir)$(ProjectName).dll&quot;" />
  <Exec WorkingDirectory="$(ProjectDir)" Command="dotnet mapster mapper -a &quot;$(TargetDir)$(ProjectName).dll&quot;" />
</Target>
```

### update the program.cs 

- make the mappings discoverable by the assembly

`config.Scan(typeof(MapsterMappings).Assembly); -- discover by asembly`

### add GenerateMapper method 

- add the generate mapper method to each configuration 

```csharp
    config.ForType<Person, PersonDto>()
        .TwoWays()
        .GenerateMapper(MapType.Map); // method creating the mappings 
```
