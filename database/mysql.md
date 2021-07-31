## Mysql Functions 

### Day name 
 gives the which day is the specific date eg:- monday tuesday , wednesday 

``` sql
SELECT member.birthdate , dayname(member.birthdate) FROM startupdocterdb.member;
```
the result output will be 

![result](../images/ms_1.png)

### char length 
 the length of string can be obtained 

 ``` sql 
 SELECT books.author_fname As 'name'  , char_length(books.author_fname) As 'length' from   mydb.books;
```

returns the output 

![result](../images/ms_2.png)

### get current time 
 returns the current date time value 

 ``` sql 
 select now();
 ```

> output  =>  '2021-07-31 11:08:54'

### add time to current time 

add specific hours / minutes / seconds to existing time 

``` sql 
select now() as currentTime ,  addtime(now() , '0:05:00') as modifiedTime
```

> output 

|currentTime        |modifiedTime       |
|-------------------|-------------------|
|2021-07-31 11:13:40|2021-07-31 11:18:40|

### substract time 
used substract time from a time 

``` sql 
select now() as currentTime ,  subtime(now() , '0:05:00') as modifiedTime
```
> output

|currentTime        |modifiedTime       |
|-------------------|-------------------|
|2021-07-31 11:17:58|2021-07-31 11:12:58|

