Let say there are two arrays...

`["Bread", "Cheese"]` and `["Tomato", "Bread"]`

Yes, We're making a sandwich.

In JavaScript if we want to combine two arrays we can simply use the .concat() method.

```js
const top = ["Bread", "Cheese"];
const bottom = ["Tomato", "Bread"];

const sandwich = top.concat(bottom);
console.log(sandwich); // ["Bread", "Cheese", "Tomato", "Bread"]
```

But what if we want to add an onion in the middle?
Now this will require some complex code to achieve...

But we can do this with a really simple ES6 Feature.

```js
const top = ["Bread", "Cheese"];
const bottom = ["Tomato", "Bread"];

const sandwich = [...top, ...bottom];
console.log(sandwich); // ["Bread", "Cheese", "Tomato", "Bread"]

// Now add Onions

const sandwichWithOnions = [...top, "Onion", ...bottom];
console.log(sandwichWithOnions); // ["Bread", "Cheese", "Onion",  "Tomato", "Bread"]
```
