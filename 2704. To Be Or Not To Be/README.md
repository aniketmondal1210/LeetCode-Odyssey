# Expect Function

## Problem Description

Write a function `expect` that helps developers test their code.  
It should take in any value `val` and return an object with the following two functions:

- **toBe(val)** → accepts another value and returns `true` if the two values are strictly equal (`===`).  
  If they are not equal, it should throw an error `"Not Equal"`.

- **notToBe(val)** → accepts another value and returns `true` if the two values are **not** strictly equal (`!==`).  
  If they are equal, it should throw an error `"Equal"`.

---

## Example 1

**Input:**
```js
func = () => expect(5).toBe(5);
```

**Output:**
```json
{"value": true}
```

**Explanation:**  
5 === 5 so this expression returns true.

---

## Example 2

**Input:**
```js
func = () => expect(5).toBe(null);
```

**Output:**
```json
{"error": "Not Equal"}
```

**Explanation:**  
5 !== null so this expression throws the error `"Not Equal"`.

---

## Example 3

**Input:**
```js
func = () => expect(5).notToBe(null);
```

**Output:**
```json
{"value": true}
```

**Explanation:**  
5 !== null so this expression returns true.

---
