## react setting up environment 

**webPack** is used to bundle all the js files to a single js file . It aslo has a web server . 

webpack configeration for the react app is created with the name [webpack.config.dev.js](https://gist.github.com/dinith72/d0473ad18aa5387b0cfe503d5b847138)

**Babel** - Babel will be used to achive two objectives . 
- convert *jsx* to the javascript code 
- convert modern javascript *ES 6+* to normal javascript

add the following code to root of *package.json*. 

``` json
 "babel": {
    "presets": [
      "babel-preset-react-app" 
    ]
  },
```
**running through npm scripts** - npm scripts can be used to automate build and the running of the application. 

create sutom script with follwing commands. 

``` json 
"start": "webpack serve --config webpack.config.dev.js --port 3000" 
```
this would show 
- the location of the webpack config file 
- port it should run 

## react concepts 

### react useref hook

**useeref hook is used to get reference to html element**- i t can be very much useful in getting values in formcontrols. 

``` ts
// declaring the red 
const nameRef = useRef<HTMLInputElement>(null); 

// connecting with html element through ref attribute 
 <input ref={nameRef} id='name' type="text" className='form-control' />

// reading the value from ref
if(nameRef.current)
    person.name = nameRef.current.value; // ref.current will return the dom element

```
> notes 

- if the linking dom element *HTmlInput* folling **HTMLInputElement** generic should be passed to the **useref hook**

### passing function as props 

> in the *typescript* version the interface for props should be defined . 

``` ts
interface ListGroupProps {
  items: string[],
  heading: string,
  onSelectItem: (item: string) => void // interface for the function
}
```
Note that we are going to pass a function which **accepts a string and return nothing**

> in the child component 

can be *destructured* and imported in props. In below **onSelectItem** is the function. 
```  ts
function ListGroup({ items, heading, onSelectItem }: ListGroupProps) { ....}
```

the function is used in **child component**. 

``` html
<li   
    key={index}
    onClick={() => {  onSelectItem(item); }}
  >
    {item}
  </li>
```

> in the parent component

``` ts
// function defined here 
  const handleSelectItem = (item: string) => console.log(item); 
  return (
    <div className='App'>
    // passed to child item here 
      <ListGroup items={items} heading='Countries' onSelectItem={handleSelectItem} />
    </div>
  );
```

### passing content from children

> child component

the following **interface** should be added. 
``` ts
interface AlertProps {
    children: string
}
```

to send html content , **type of children** should be changed **to ReactNode** 

``` ts
interface AlertProps {
    children: ReactNode
}
```

> parent component 

values can be passed as children. 

``` html
<div className='App'>
      <Alert>
        sample text
      </Alert>

    </div>
```


**children** is special property which let you pass items as children.

### updating state of nested objects 

when updating the state of a nested object , **each of the object shouuld be recreated** as the *spread operator will do shallow copy: it will copy address of the child objects*.

usecase : copying of person details 

``` ts 
  // person detail object strucure 
let { customer, setCustomer } = useState({
    name: 'dinith',
    address: {
      street: '140/3, Kandy road',
      zipCode: 11870
    }
  });
    // method to update state
  const handleCustomer = () => {
    setCustomer({
      ...customer,
      // address object has to created as a new object since spread operator will point to same object
      address: {
        ...customer.address,
        zipCode: 12070
      }
    })
  }
  ```

Here

 - the spread operator will return the *existing address* object.
 - since state update needs a new object always.
 - a **new object should be created** explicitely
 - if there are multiple objects this should be done.

### updating state of an array 

if state of array of items needs to be updated , it should be done **without modifying** the existing array. 

 ### updating state using [immer](https://immerjs.github.io/immer/)

 immer can be used to update the **state in mutable way**. underthehood immer will *translate to a immutable state update*. 

 sample code snippet showing how to update state using immer is shown [here](https://gist.github.com/dinith95/4d845e0de1a5ddb07d39b6599aea1e87#file-update-with-immer-tsx)


## react inbuilt components 

### react router 

**react router** can be used to navigate in between different web pages . 

**Switch** this will traverese from top to down and navigate the route which mateches first . 

see the below [react router example](https://gist.github.com/dinith72/aaffbfb2ae1d0609ee1058e9f5decfbf)

### react strictMode

- once it is enabled **all the components are rendered twice** .
- each component is rendered twice to **identify any errors done while creating components**. 
 - effects of this are only applied in the *development environment* .



