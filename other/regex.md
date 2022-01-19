
## regex match  characters 

**.**  -   any character 

**\\**  - escape a special character

**\d** - any digit

**\D** - not a digit

**\w** - character insides following criteria [a-z] , [A-Z] , [0-9] , _ *( any word character )*

**\W** - any non word character

**\s** - any space ( space , tab . new line )

**\S** - anything not a  space ( space , tab . new line )

## regex position characters

**\b** - begining of a word or end of a word

**^** - begining of a line 

**$**  - end of a line

## regex group characters 

**[ ]** - any character in the square bracket 

**[1-9]** - any character in between the range 
```
    ex : [a-f] - any character in between a and f
         [1-5] - any number in between 1 and 5 
         [a-fA-F] - any character in between a and f and A and F

```
**[^ ] - any charater range not in the set 
    ex : [^a-f] - all the characters not in a nd f range 

## regex quantifiyers 

**+** - 1 or more similar characters 

**\*** - 0 or more similar characters 

**{3}** - exact count 

**{3,5}** - range ( 3 to 5 characters )
