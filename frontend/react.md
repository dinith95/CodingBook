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


## react inbuilt components 

### react router 

**react router** can be used to navigate in between different web pages . 

**Switch** this will traverese from top to down and navigate the route which mateches first . 

see the below [react router example](https://gist.github.com/dinith72/aaffbfb2ae1d0609ee1058e9f5decfbf)



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

