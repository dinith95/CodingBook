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
