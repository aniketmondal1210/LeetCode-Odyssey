# Find the Index of the k-th Occurrence of an Element

## Problem

You are given:

- An integer array `nums`
- An integer array `queries`
- An integer `x`

For each query `queries[i]`, find the index of the **queries[i]th occurrence** of `x` in `nums`.

If there are fewer than `queries[i]` occurrences of `x`, return `-1` for that query.

Return the resulting array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
```

**Output**

```text
[0,-1,2,-1]
```

**Explanation**

Occurrences of `1` are at indices:

```text
[0, 2]
```

Queries:

```text
1st occurrence → index 0
3rd occurrence → doesn't exist → -1
2nd occurrence → index 2
4th occurrence → doesn't exist → -1
```

---

### Example 2

**Input**

```text
nums = [1,2,3]
queries = [10]
x = 5
```

**Output**

```text
[-1]
```

**Explanation**

`5` does not occur in the array.

---

## Constraints:

- 1 <= nums.length, queries.length <= 10^5
- 1 <= queries[i] <= 10^5
- 1 <= nums[i], x <= 10^4

---
