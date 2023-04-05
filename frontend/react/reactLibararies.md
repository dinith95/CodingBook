

## react bootstrap - components 

react bootstrap can be added ``` npm install  bootstrap ```

add following line to the **index.js / index.ts** - ```import 'bootstrap/dist/css/bootstrap.css';```


## styling in react - scss 

scss can be added by the command ``` npm i sass ```

Then

- rename all the .css file to **.scss**
- update the file import css files with new name 


## fontawesome icons 

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

## react icons 
react icons consist of icons from the major icon libraries and can be used easily . 

- to install run following script ```npm install react-icons --save```

- improting icons to the application 

``` tsx
import { AiFillHeart } from 'react-icons/ai' // import the icon that is needed

// icon can be directly used as react element
 return ( <AiFillHeart size='40' color='red' onClick={handleClick} />)

```

**Notes**

- when the icons are imported select the *correct distribution* , destribution can be taken from *first 2 letters of icon name* . 
eg : for *AiFillHeart* => destribution is *ai*


## react hook from 

react hook form is very much useful in the form contraling and handling . it presents many beautiful methods to 
 - catch form updates 
 - validate the textual content

``` ts
// destructuring and getting props and methods from use form
 const {register,handleSubmit, formState: {errors}} = useForm<FormData>();

```
### [register method](https://www.react-hook-form.com/api/useform/register/) 

through this method you can register to *input field* or *select* and apply the validation and form control rules. 

register method accepts 
> name 

- the name of the input control

> html validator propertese 

- diffrent validator propertese such as => ```required: true, min: 3```

### [handle submit](https://www.react-hook-form.com/api/useform/handlesubmit/)

this will recive data in input when , 
- submit button is clicked 
- form validation is successful

### [form state](https://www.react-hook-form.com/api/useformstate/)
thorugh this we can access the *form state of each of controllers*

the **errors** property shows the *list of errors in current form state*. 

``` ts 
// declaring the above items in input control
<input 

// object return from register method is destructured
    {...register('name',{required:true, minLength:3})} 
    id='name' 
    type="text" 
    className='form-control' 
/>

// sample validation logic 
{errors.name?.type === 'required' && <small className='text-danger'> name is required </small>}
```

[sample code](https://gist.github.com/dinith95/4d845e0de1a5ddb07d39b6599aea1e87#file-same-react-hookform-tsx) showing the sample form with **react-hook-form** . 






