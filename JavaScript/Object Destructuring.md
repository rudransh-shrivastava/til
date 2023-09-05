We sometimes need to create variables for the properties of an object
This is the normal way of doing it.
```js
const operatingSystems {
    windows: 'bloatware',
    manjaro: 'sucks',
    arch: 'I use arch btw',
}

const windows = operatingSystems.windows;
const manjaro = operatingSystems.manjaro;
const arch = operatingSystems.arch;
```

But with the new ES6 we can write this in a more compact way like this!
```js
const operatingSystems {
    windows: 'bloatware',
    manjaro: 'sucks',
    arch: 'I use arch btw',
}

const {windows, manjaro, arch} = operatingSystems;
```

B-But what if I wish to name them differently?
Use a semi colon to use custom names.
```js
const {windows: lag} = operatingSystems;
console.log(lag); // output: bloatware
```
