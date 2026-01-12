# In Memory Caching  

- requests can be cached in memory so that performance can be optimized as it dosent need to hit database / api always 
- cached on the memory of the application 
- caching cocs - [microsft docs ](https://learn.microsoft.com/en-us/dotnet/core/extensions/caching#in-memory-caching)
- code sample - [basic caching](https://gist.github.com/dinith95/b77938a35a5fcfcbe956c517f7738b3a#file-basiccaching-cs)

## Expiration Types 

### Absolute Expiration
- after a given time from he set date cache value is expired 
- [code sample](https://gist.github.com/dinith95/b77938a35a5fcfcbe956c517f7738b3a#file-absoluteexpire-cs)

### Sliding Expiration 

- cached will be expired from given time period is **elapsed from last access time**
- if the absolute expiration reached before it it would be expired.
- [code sample](https://gist.github.com/dinith95/b77938a35a5fcfcbe956c517f7738b3a#file-slidingexpire-cs)
  


