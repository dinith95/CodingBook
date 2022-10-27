# Foundational concepts 

## Execution context 

when a block of code is given for the execution , the js compiler will goes through it line by line and assign any varaibles to the memory . This execution process is called the **Thread of Executioion**.

sample code 
``` js
const num = 1;
function multBy2(num){
  const result = num * 2;
  return result;
}
const name = 'dinith';
const output = multBy2(4);
```
> Execution steps 
1. Add tne variable **num** to memory and assign  1
2. Assign the function **MultBy2** to memory as a label ( function is not parsed until it is called.)
3. Add tne variable **name** to memory and assign  'dinith'.
4. Add tne variable **output** to memory ( global execution context ) and assign  *undefined* as its value is yet to be evaluated.
5. create a **new execution context** and start evaluating the **MultBy2 function**.

The *Memory and Thread of Execution* is know as the **The execution context**.

> Note ->  the initial execution contect that program statis an *Global Ececution context* . 

## Generator Function

Generator functions executes code in between perticular *yeild* statments .

yield - will return the any value computed from the function logic  and it stops excution of the next coding .  

### Function Syntax

``` javascript
function* simpleGenerator(b){
  // programming logic .....
  yield b*1
  // programming logic .....
  yield b*2
  // programming logic .....
  yield b*3
}
```

> Note - **the * mark is added to the end of the function to denote that it is Generator function**.

> Note - the generator function can be called by using the `next()` method in the object .

> Note the generator function returns 2 values ,
    - return value of the function
    - **done**  - indicating whether there is more code to execute.

### Invocation of the Function

``` javascript
const genObj1 = simpleGenerator(3); // trturn the generator function object 
console.log(genObj1.next()); // { value: 3, done: false }
console.log(genObj1.next()); // { value: 6, done: false }
console.log(genObj1.next()); // { value: 9, done: false }
console.log(genObj1.next());// { value: undefined, done: true }
```

### Multiple Object creation

Multiple object created on the same function will be having seperate instance.
[sample code multiple object](https://replit.com/@dinith72/GeneratorFunction#generatorMultiple.js)

### passing value to through yield

a value can be passed to yield with the below syntax.

``` javascript
function* sampleGen1() {
  let id = 0;
  while (1) {
    const inc = yield id; // this will assign the passed in value from next function
    if (inc != null) {
      id += inc;
    }
    else {
      id++;
    }
  }
}
```

[passing-values-code-sample]()

### Infinite Iterator
an infinite iterator can be created which would give return incremental value when required. 
[sample infinite loop](https://replit.com/@dinith72/GeneratorFunction#infiniteLoop.js)
