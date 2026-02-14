- way to create more descriptive name for an **existing type or combination of types**
- premitives can be renmed as `type UserID = string;`

## Tuples

- special type of array with **fixed number of elements** and **known types** at each index.
- each position in the tuple can have a different type.
- example

```typescript
let person: [string, number] = ["Alice", 30];
```

- **Rest elements** can be defined in tuples using `...` syntax.
- combine the fixed elements with variable-length elements.

```typescript
type Scores = [string, ...number[]];
const player1: Scores = ["Alice", 10, 20, 30]; // valid tuple
const player2: Scores = ["Bob", 10]; // valid tuple
const player3: Scores = ["Charlie", "Bob", 10]; // invalid tuple has more than 1 string
```

## Record Types

- utility type that allows you to create an object type with specified keys and values.
- defined using `Record<Keys, Type>` syntax
- can have any number of keys, but keys **must be of the same type** and values must be of the same type as well.

```typescript
var empData: Record<string, string | number> = {
  name: "Jane Doe",
  empId: 34,
  age: 30,
};
```

## Not Null Types

- specifies that a value cannot be `null` or `undefined`.
- indicated using `{}` after the type.

```typescript
let val: {} = "test"; // valid assignment
val = 123; // valid assignment
val = null; // invalid assignment, cannot assign null
val = undefined; // invalid assignment, cannot assign undefined
```

## Union Types

- this expresses as value can be one of several types .
- types can be combined using `|` operator.
- example

```typescript
let age: number | string = 30; // union type
age = "thirty"; // valid assignment due to union type
age = false; // invalid assignment, will cause a type error
```

- union types can be assigned to array as well

```typescript
let mixedArray: (number | string)[] = [1, "two", 3]; // valid array with union types
```
