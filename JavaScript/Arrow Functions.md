With the new ES6, there's a simpler way of defining functions => using arrow functions.

Take a look at this code.

```js
const square = functions(number) {
    return number * number;
}
```
We can simplify this function using the following steps:

The first step is to remove the `functions` keyword.
```js
const square = (number) {
    return number * number;
}
```

Then, we must add an arrow like so.
```js
const square = (number) => {
    return number * number;
}
```

Since there's only one parameter, we can remove the ().
```js
const square = number => {
    return number * number;
}
```

If there's only a single line of code and it returns a value, we can remove the `return` keyword.
```js
const square = number => {
    number * number;
}
```

We can also remove the {}.
```js
const square = number => number * number;
```

Now, we can finally write this exact code but in a way cleaner and compact way like this!
```js
const square = number => number*number;
```
