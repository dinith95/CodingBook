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


### Page layout with multiple columns

page can be designed with multiple coloumns by using the **minipage** command . 

``` 
\begin{minipage}{<width>}
 \framebox(325,\boxHight){}
\end{minipage} 

```

> Note - dont leave space b/w 2 minipage tags , it will cause it go to next page . 

### Add page header footer 

use the package **fancyhdr** 

> include section - ``` \usepackage{fancyhdr} ```

> update pagestyle - ``` \pagestyle{fancy} ```

> add header on center - ``` \chead{< header content > } ```

> add footer on center - ``` \cfoot{< header content>} ```

*Note* - 

to remove the top bar autmatically added with header - ``` \renewcommand{\headrulewidth}{0pt} ```



## Lines and shapes 

### Horizontal Line 

Horizontal line can be added 

``` \noindent\rule{15cm}{1.5pt} ```

here *noindent* will remove all the indentation

### empty box

use the **framebox** to add a empty text box

``` \framebox(<width> ,<height>){} ```

*Note* when adding mulitple boxes there is a space in between boxes , to avoid add **%** character at the end . 

``` \framebox(40,\boxHight){}% ```



## Text Formattings 

### Text Layaout 

the text layout can be aligned using the value passed to the begin command . 

``` 
 \begin{flushright}
        \textbf{9084/32 }
 \end{flushright}

```

> alight left - ``` flushleft ```

> align right - ``` flushright ```



## other
### Varaibles 

Add the varaibles to the page by adding following command in import section

``` \newcommand{\newCommandName}{text to insert} ```


