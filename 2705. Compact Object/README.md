# Compact Object (Remove Falsy Values Recursively)

## Problem Statement
Given an **object or array `obj`**, return a **compact object**.

A **compact object** is the same as the original, **but with all keys whose values are falsy removed**.  
This rule applies **recursively** to:

- nested objects  
- nested arrays  

In JavaScript, a value is **falsy** if:

Boolean(value) === false

Examples of falsy values: `null`, `0`, `false`, `""`, `undefined`, `NaN`.

You may assume the input is valid JSON (i.e., only objects, arrays, numbers, strings, booleans, null).

---

## Example 1

**Input:**

obj = [null, 0, false, 1]


**Output:**

[1]


**Explanation:** All falsy values are removed from the array.

---

## Example 2

**Input:**

obj = {"a": null, "b": [false, 1]}


**Output:**

{"b": [1]}


**Explanation:**  
- `"a"` is removed (value is null)  
- `b[0]` is removed (false)

---

## Example 3

**Input:**

obj = [null, 0, 5, [0], [false, 16]]


**Output:**

[5, [], [16]]


**Explanation:**  
Removed falsy elements while keeping structure intact:
- `obj[0]`, `obj[1]`, `obj[3][0]`, `obj[4][0]` were removed.

---

## Constraints

- obj is valid JSON
- 2 ≤ JSON.stringify(obj).length ≤ 10⁶


---
