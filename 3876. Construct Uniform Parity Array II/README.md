# Same Parity Array

## Problem

You are given an array `nums1` of `n` distinct integers.

You need to construct another array `nums2` of length `n` such that all elements of `nums2` are either **odd** or **even**.

For every index `i`, you must choose exactly one of the following:

- `nums2[i] = nums1[i]`
- `nums2[i] = nums1[i] - nums1[j]`, where `j != i` and `nums1[i] - nums1[j] >= 1`

Return `true` if it is possible to construct `nums2` such that all its elements have the same parity. Otherwise, return `false`.

---

## Examples

### Example 1

**Input:**
```text
nums1 = [1, 4, 7]
```

**Output:**
```text
true
```

**Explanation:**

We can construct:

```text
nums2[0] = nums1[0] = 1
nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3
nums2[2] = nums1[2] = 7
```

Therefore:

```text
nums2 = [1, 3, 7]
```

All elements are odd, so the answer is `true`.

---

### Example 2

**Input:**
```text
nums1 = [2, 3]
```

**Output:**
```text
false
```

**Explanation:**

It is not possible to construct `nums2` such that all elements have the same parity.

---

### Example 3

**Input:**
```text
nums1 = [4, 6]
```

**Output:**
```text
true
```

**Explanation:**

We can simply choose the original values:

```text
nums2 = [4, 6]
```

Both elements are even, so the answer is `true`.

---

## Constraints

- `1 <= n == nums1.length <= 10^5`
- `1 <= nums1[i] <= 10^9`
- `nums1` consists of distinct integers.

---
