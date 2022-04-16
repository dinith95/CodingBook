## react useful libraries  

### react bootstrap - components 

react bootstrap can be added ``` npm install react-bootstrap bootstrap ```


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

