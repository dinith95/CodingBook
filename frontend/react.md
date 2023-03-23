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


## react inbuilt components 

### react router 

**react router** can be used to navigate in between different web pages . 

**Switch** this will traverese from top to down and navigate the route which mateches first . 

see the below [react router example](https://gist.github.com/dinith72/aaffbfb2ae1d0609ee1058e9f5decfbf)



## react useful libraries  

### react bootstrap - components 

react bootstrap can be added ``` npm install  bootstrap ```

add following line to the **index.js / index.ts** - ```import 'bootstrap/dist/css/bootstrap.css';```


### styling in react - scss 

scss can be added by the command ``` npm i sass ```

Then

- rename all the .css file to **.scss**
- update the file import css files with new name 


### fontawesome icons 

the fontawsome can be added with below steps mentioned in [fontawsome install page](https://fontawesome.com/v6/docs/web/use-with/react/). 

In this method all the icons are **imported dynamically**.

**Notes** 

> Adding Babel config

if the file *babel.config.js* does not exist - **create babel.config.js on src folder**

> adding babel-plugin-macros.config.js

create the **babel-plugin-macros.config.js** on the **src folder**

 when using the icons use following snippet 

 ```JSX
// importing icons 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { solid, regular,  brands } from '@fortawesome/fontawesome-svg-core/import.macro'

// using icons 
 <FontAwesomeIcon icon={brands('linkedin')} />
```

