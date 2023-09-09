Sometimes we lose `this` because we pass the method somewhere outside the object, a common way to fix this is by using the `bind()` method.

This is the syntax:

```js
let player = {
  name: "Rob",
  age: 28,
};

function playerGreet() {
  console.log(`Hello ${this.name}, you are ${this.age} years old!`);
}

let playerGreetFunc = playerGreet.bind(player);

playerGreetFunc(); // Hello Rob, you are 28 years old!
```
