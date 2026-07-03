# Apply Operations to an Array

## Problem

You are given a 0-indexed array `nums` of non-negative integers.

Perform `n - 1` operations sequentially:

- If `nums[i] == nums[i + 1]`, then:
  - Multiply `nums[i]` by `2`.
  - Set `nums[i + 1]` to `0`.
- Otherwise, do nothing.

After all operations, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

Return the resulting array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,2,1,1,0]
```

**Output**

```text
[1,4,2,0,0,0]
```

**Explanation**

Operations performed:

```text
[1,2,2,1,1,0]
      ↓
[1,4,0,1,1,0]
          ↓
[1,4,0,2,0,0]
```

After shifting all zeros to the end:

```text
[1,4,2,0,0,0]
```

---

### Example 2

**Input**

```text
nums = [0,1]
```

**Output**

```text
[1,0]
```

**Explanation**

No merge operation is possible. Simply move the zero to the end.

---

## Constraints:

- 2 <= nums.length <= 2000
- 0 <= nums[i] <= 1000

---
