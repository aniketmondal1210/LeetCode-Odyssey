# Divide a String Into Groups of Size `k`

## Problem Statement
A string `s` can be partitioned into groups of size `k` using the following rules:

1. The first group contains the first `k` characters of `s`.
2. The second group contains the next `k` characters, and so on.
3. Each character belongs to exactly one group.
4. If the last group has fewer than `k` characters, a **fill character** is appended until the group size becomes `k`.
5. After removing the fill characters (if any) from the last group and concatenating all groups, the result must be the original string `s`.

Given:
- a string `s`
- an integer `k`
- a character `fill`

Return a string array representing all the groups.

---

## Examples

### Example 1
**Input:**

s = "abcdefghi"
k = 3
fill = "x"


**Output:**

["abc", "def", "ghi"]


**Explanation:**
- All groups are fully filled using characters from `s`
- No fill characters are required

---

### Example 2
**Input:**

s = "abcdefghij"
k = 3
fill = "x"


**Output:**

["abc", "def", "ghi", "jxx"]


**Explanation:**
- The last group has only one character `"j"`
- Two fill characters `"x"` are added to complete the group

---

## Constraints

- 1 <= s.length <= 100
- s consists of lowercase English letters only
- 1 <= k <= 100
- fill is a lowercase English letter


---
