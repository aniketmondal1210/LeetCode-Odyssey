# Duplicate Zeros

## Problem

Given a fixed-length integer array `arr`, duplicate each occurrence of `0`, shifting the remaining elements to the right.

Elements beyond the original length of the array are discarded. Modify the array **in-place** without returning anything.

---

## Examples

### Example 1

**Input**

```text
arr = [1,0,2,3,0,4,5,0]
```

**Output**

```text
[1,0,0,2,3,0,0,4]
```

**Explanation**

Each `0` is duplicated, and the remaining elements are shifted to the right. Elements exceeding the array length are discarded.

---

### Example 2

**Input**

```text
arr = [1,2,3]
```

**Output**

```text
[1,2,3]
```

**Explanation**

There are no zeros to duplicate, so the array remains unchanged.

---

## Constraints:

- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 9

---
