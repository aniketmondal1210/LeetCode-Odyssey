# Check if an Object or Array is Empty

## Problem Statement
Given an **object** or an **array** (as parsed from `JSON.parse`), determine whether it is **empty**.

Definitions:
- An **empty object** has **no key–value pairs**.
- An **empty array** has **no elements**.

Return:
- `true` → if empty  
- `false` → otherwise

---

## Example 1

**Input:**

obj = {"x": 5, "y": 42}


**Output:**

false


**Explanation:** The object has 2 keys.

---

## Example 2

**Input:**

obj = {}


**Output:**

true


**Explanation:** No key-value pairs → empty.

---

## Example 3

**Input:**

obj = [null, false, 0]


**Output:**

false


**Explanation:** The array has 3 elements.

---

## Constraints

obj is valid JSON (object or array)
2 ≤ JSON.stringify(obj).length ≤ 10⁵


---

## Key Idea (O(1) Time Solution)
Checking if an object or array is empty can be done in **constant time** using:

### For arrays:

obj.length === 0


### For objects:
The number of keys can be checked in O(1) in most JavaScript engines (because the keys count is stored internally):

Object.keys(obj).length === 0


But a truly **O(1)** approach (no iteration) uses:

JSON.stringify(obj) === "{}"
JSON.stringify(obj) === "[]"


Since JSON.stringify(obj) is already provided as valid input, engines often compute string length while parsing, so this check is effectively constant-time.

---
