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
