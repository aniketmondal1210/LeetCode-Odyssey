# Special Array I

## Problem

An array is considered **special** if every pair of adjacent elements has **different parity**.

In other words, for every adjacent pair:

- One element must be **even**.
- The other element must be **odd**.

Given an integer array `nums`, return:

- `true` if `nums` is a special array.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
nums = [1]
```

**Output**

```text
true
```

**Explanation**

The array contains only one element, so there are no adjacent pairs to check.

---

### Example 2

**Input**

```text
nums = [2,1,4]
```

**Output**

```text
true
```

**Explanation**

Adjacent pairs are:

```text
(2,1) → Even, Odd ✓
(1,4) → Odd, Even ✓
```

Every adjacent pair has different parity.

---

### Example 3

**Input**

```text
nums = [4,3,1,6]
```

**Output**

```text
false
```

**Explanation**

Adjacent pairs are:

```text
(4,3) → Even, Odd ✓
(3,1) → Odd, Odd ✗
```

Since two adjacent elements have the same parity, the array is not special.

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---
