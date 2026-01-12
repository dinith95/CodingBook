# Testing types - Fact 
- single piece of logic
- annotaged with the attribute `[Fact]`
- one set of input data and assertions based on it 
- [code sample](https://gist.github.com/dinith95/efac6a188827693b37cc5ed6d7f6fb0b#file-facttest-cs)  

# Testing types - theory
- test **multiple logics** along with negative scenarios
- annotated with attribute `[Theory]`
- multiple sets of input data
- 3 methods of passing data 
  - InlineData
  - MemberData : values from a method
  - Class Data : values from a class

## Inline Date 
- values passed as attributes to methods 
- [code sample](https://gist.github.com/dinith95/efac6a188827693b37cc5ed6d7f6fb0b#file-theoryinlinedata-cs)

## MembersDate 
- values passed as retrun values from a method 
- method should always return `IEnumerable<object[]>`
- [code sample](https://gist.github.com/dinith95/efac6a188827693b37cc5ed6d7f6fb0b#file-theorymmeberdata-cs)

## Class Data 
- Supplies data from a separate class that implements `IEnumerable<object[]>`
- [code sample](https://gist.github.com/dinith95/efac6a188827693b37cc5ed6d7f6fb0b#file-theoryclassdatatest-cs)