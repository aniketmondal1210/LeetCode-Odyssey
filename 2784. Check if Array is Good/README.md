# Check if Array is Good

## Problem Statement

An array `nums` is called **good** if it is a permutation of:

```text
base[n] = [1, 2, 3, ..., n-1, n, n]
```

Meaning:

- Numbers from `1` to `n-1` appear exactly once
- Number `n` appears exactly twice

Return `true` if `nums` is good, otherwise return `false`.

---

# Examples

### Example 1

```text
Input:
nums = [2,1,3]

Output:
false
```

### Explanation

```text
max(nums) = 3

base[3] = [1,2,3,3]
Length should be 4, but nums length is 3.
```

---

### Example 2

```text
Input:
nums = [1,3,3,2]

Output:
true
```

---

### Example 3

```text
Input:
nums = [1,1]

Output:
true
```

---

## Constraints:

- 1 <= nums.length <= 100
- 1 <= num[i] <= 200

---
