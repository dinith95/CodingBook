# Basics

## passing variables 

varaibles can be passed from logic component to template as follows . 

> template file ( .html file )

``` html
<div class="container">
 <div class="col">
   <!-- the item count , should be in double paranthesis -->
   <p> Add a list of activities {{itemCount}} </p>
 </div>
</div>
```

``` Typescript
export class HomeComponent implements OnInit {
 itemCount : number = 4 ; // item count is declared here

 constructor() { }

 ngOnInit() {}

}

```

## passing events 

Events triggered in the template file can be passed from template file to logic file . 

```html
<input type="submit" class="btn" [value]= btnTextAdd (click)="addItem()"> 
<!-- click event add item is passed as shown below-->
```

## ngFor

**ngfor** can be used to iterate over list in logic file ( ts file)

```html
<mat-menu #appMenu="matMenu" class="actionMenu" >
    <!-- iterating over array of menuItems  -->
    <button *ngFor="let item of menuItems"  >{{item}}</button>         
</mat-menu>
```