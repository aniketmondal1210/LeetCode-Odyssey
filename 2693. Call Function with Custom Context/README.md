# Function.prototype.callPolyfill

## Problem

Enhance all functions with a method:

```javascript
callPolyfill
```

which behaves like JavaScript's built-in:

```javascript
Function.prototype.call()
```

but **without using the built-in `call` method**.

The method:

- Takes an object `obj` as the first argument.
- Uses `obj` as the `this` context.
- Passes all remaining arguments to the function.

---

## Example 1

### Input

```javascript
fn = function add(b) {
    return this.a + b;
}

fn.callPolyfill({ a: 5 }, 7);
```

### Output

```javascript
12
```

### Explanation

```javascript
this = { a: 5 }
b = 7

5 + 7 = 12
```

---

## Example 2

### Input

```javascript
fn = function tax(price, taxRate) {
    return `The cost of the ${this.item} is ${price * taxRate}`;
}

fn.callPolyfill({ item: "burger" }, 10, 1.1);
```

### Output

```javascript
"The cost of the burger is 11"
```

---

## Constraints:

- typeof args[0] == 'object' and args[0] != null
- 1 <= args.length <= 100
- 2 <= JSON.stringify(args[0]).length <= 10^5

---
