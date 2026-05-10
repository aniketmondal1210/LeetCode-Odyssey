# Construct Array with Reverse Copy

## Problem Statement

You are given an integer array `nums` of length `n`.

Create a new array `ans` of size `2 * n` such that:

```text
First n elements  -> same as nums
Next n elements   -> nums in reverse order
```

Formally:

```text
ans[i] = nums[i]
ans[i + n] = nums[n - i - 1]
```

Return the array `ans`.

---

# Examples

### Example 1

```text
Input:
nums = [1,2,3]

Output:
[1,2,3,3,2,1]
```

### Explanation

```text
Original part : [1,2,3]
Reverse part  : [3,2,1]
```

Combined:

```text
[1,2,3,3,2,1]
```

---

### Example 2

```text
Input:
nums = [1]

Output:
[1,1]
```

---

# Constraints

```text
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

---
