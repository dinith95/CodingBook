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