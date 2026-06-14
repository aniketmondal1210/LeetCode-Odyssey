# Memoize Function

## Problem

Given a function `fn`, return a **memoized** version of that function.

A memoized function stores the results of previous function calls and returns the cached result whenever it is called again with the same arguments.

Two inputs are considered identical if they are compared equal using:

```javascript
===
```

---

## Example 1

### Input

```javascript
fn = function (a, b) {
    return a + b;
}
```

Calls:

```javascript
memoized(2, 2);
memoized(2, 2);
memoized(1, 2);
```

### Output

```javascript
4
4
3
```

### Explanation

```text
(2,2) -> computed and cached
(2,2) -> returned from cache
(1,2) -> computed and cached
```

---

## Example 2

### Input

```javascript
memoized({}, {});
memoized({}, {});
memoized({}, {});
```

### Explanation

Each object is a different reference:

```javascript
{} === {} // false
```

Therefore every call is treated as unique.

---

## Example 3

### Input

```javascript
const o = {};

memoized(o, o);
memoized(o, o);
memoized(o, o);
```

### Explanation

The same object references are used:

```javascript
o === o // true
```

So only the first call executes `fn`.

---

## Constraints:

- 1 <= inputs.length <= 10^5
- 0 <= inputs.flat().length <= 10^5
- inputs[i][j] != NaN

---
