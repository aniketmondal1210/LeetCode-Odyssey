# Find Unique Binary String

## Problem

Given an array of strings `nums` containing `n` **unique** binary strings, where each string has length `n`, return a binary string of length `n` that **does not appear** in `nums`.

If there are multiple valid answers, you may return any of them.

### Example 1

**Input:**
```text
nums = ["01","10"]
```

**Output:**
```text
"11"
```

**Explanation:**  
`"11"` does not appear in `nums`. `"00"` would also be correct.

### Example 2

**Input:**
```text
nums = ["00","01"]
```

**Output:**
```text
"11"
```

**Explanation:**  
`"11"` does not appear in `nums`. `"10"` would also be correct.

### Example 3

**Input:**
```text
nums = ["111","011","001"]
```

**Output:**
```text
"101"
```

**Explanation:**  
`"101"` does not appear in `nums`. `"000"`, `"010"`, `"100"`, and `"110"` would also be correct.

---

## Approach

A simple and elegant solution is to use **Cantor's Diagonalization**.

For every index `i`:

- Look at the `i`-th character of `nums[i]`.
- Make the `i`-th character of our answer the **opposite**:
  - If `nums[i][i] == '0'`, put `'1'`.
  - If `nums[i][i] == '1'`, put `'0'`.

This guarantees that the generated string differs from `nums[i]` at position `i`.

Therefore, the resulting string cannot be equal to any string in `nums`.

### Example

For:

```text
nums = ["111", "011", "001"]
```

Take the diagonal characters:

```text
nums[0][0] = '1'
nums[1][1] = '1'
nums[2][2] = '1'
```

Flip each character:

```text
1 -> 0
1 -> 0
1 -> 0
```

So one valid answer is:

```text
"000"
```

`"000"` is not present in `nums`.

---

## Java Solution

```java
class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i].charAt(i) == '0') {
                ans.append('1');
            } else {
                ans.append('0');
            }
        }

        return ans.toString();
    }
}
```

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` for the resulting string.

Since `n <= 16`, this approach is very efficient.

---

## Key Idea

> Flip the diagonal character `nums[i][i]` for every `i`.

The answer is guaranteed to be different from every string in `nums` because it differs from `nums[i]` at index `i`.
