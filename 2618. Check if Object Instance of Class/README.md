# Check If Value Is an Instance of a Class

## Problem

Write a function `checkIfInstanceOf(obj, classFunction)` that returns `true` if:

- `obj` is an instance of `classFunction`, or
- `obj` is a primitive value that has access to the methods of its wrapper object (e.g., `5` and `Number`).

Otherwise, return `false`.

---

## Examples

### Example 1

**Input**

```javascript
checkIfInstanceOf(new Date(), Date)
```

**Output**

```javascript
true
```

---

### Example 2

**Input**

```javascript
class Animal {}
class Dog extends Animal {}

checkIfInstanceOf(new Dog(), Animal)
```

**Output**

```javascript
true
```

---

### Example 3

**Input**

```javascript
checkIfInstanceOf(Date, Date)
```

**Output**

```javascript
false
```

---

### Example 4

**Input**

```javascript
checkIfInstanceOf(5, Number)
```

**Output**

```javascript
true
```

**Explanation**

Although:

```javascript
5 instanceof Number // false
```

the number `5` still has access to `Number` methods through boxing, so it is considered an instance for this problem.

---
