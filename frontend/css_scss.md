## CSS Selector types

### By attribute 

select the element containing the an attribute. 

eg : containing *href* attribute

```css
[href] {
  color: red;
}
```
through the **value in an attribute**, 

eg : containing *value about.html in href* attribute

```css
[href="about.html"] {
  color: red;
}
```

### child selector

child selector demo is available at [child selector demo](https://codepen.io/dinith72/pen/xxRyLob)

uses the sumbol ">". \
select the elements which are **only direct children** 

```css
.direct-children > p {
  color: green;
}
```

select the element number which satistfy the condition

example : select **2nd h1** element

```css 
h1:nth-child(2) {
  opacity: 1 !important;
 }
```



## Animations in CSS 

### Transform Animations 

these will define the motion , size change , rotation , skew like propertese . 
full documentation is available in [w3 demo page](https://www.w3schools.com/cssref/playdemo.asp?filename=playcss_transform&preval=translate(20px,10px))

to make the transform smooth **transition** can be used . See the [transform_demo](https://codepen.io/dinith72/pen/WNogjjB)


### Keyframe Animations 

a demo of this can be founf in [keyframe demo](https://codepen.io/dinith72/pen/BaJGGRM)

we can defines diffrent css propertese for each of the stages of animation through **keyframes**.

```css

h1 {
    /* defines animations name , single animation time , number of loops */
   animation: blink 6s infinite; 
}

/* propertese at different stages  */
@keyframes blink {
  0% {opacity : 0;}
  /* 0 sec => 1.5 sec : opcity 0 => 1 */
  25% {opacity : 1;}
  75% {opacity : 1;}
  /* 4.5 sec => 6 sec : opcity 1 => 0 */
  100% {opacity : 0;}
}