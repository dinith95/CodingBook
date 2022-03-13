## page propertese

### page size 

leagle size document 

``` \usepackage[legalpaper, portrait, margin=2in]{geometry}```

### page margins 

giving the custom margins : 

```
\usepackage{geometry}
\geometry{
 a4paper,
 top=1.5cm
 }

 ```

 ### Linking a another page

 create a page without 
  -  \documentclass 
  - \begin{document} 
  -  \end{document}
  
  Create a **new page** and import content

  ``` \include{page1} ```

  add content without a new page 

  ``` \input{page1} ```


## Lines and shapes 

### Horizontal Line 

Horizontal line can be added 

``` \noindent\rule{15cm}{1.5pt} ```

here *noindent* will remove all the indentation


## other
### Varaibles 

Add the varaibles to the page by adding following command in import section

``` \newcommand{\newCommandName}{text to insert} ```


