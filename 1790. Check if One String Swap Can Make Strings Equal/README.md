# Check if Two Strings Can Be Made Equal With One Swap

## Problem Statement

You are given two strings **s1** and **s2** of equal length.

A **string swap** means choosing two indices in a string and swapping the characters at those indices.

Return **true** if it is possible to make both strings equal by performing **at most one swap on exactly one string**, otherwise return **false**.

---

## Examples

### Example 1
**Input**
```
s1 = "bank"
s2 = "kanb"
```

**Output**
```
true
```

**Explanation**

Swap characters at index **0** and **3** in `"kanb"` → `"bank"`.

---

### Example 2
**Input**
```
s1 = "attack"
s2 = "defend"
```

**Output**
```
false
```

**Explanation**

More than one swap would be required.

---

### Example 3
**Input**
```
s1 = "kelb"
s2 = "kelb"
```

**Output**
```
true
```

**Explanation**

Both strings are already equal, so **no swap is needed**.

---

## Constraints:

- 1 <= s1.length, s2.length <= 100
- s1.length == s2.length
- s1 and s2 consist of only lowercase English letters.

---
