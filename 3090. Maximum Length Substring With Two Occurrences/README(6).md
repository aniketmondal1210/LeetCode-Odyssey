# Problem: Maximum Length Substring With At Most Two Occurrences

## Problem Statement

Given a string `s`, return the **maximum** length of a substring such that it contains **at most two occurrences of each character**.

---

## Example 1

**Input:**

```text
s = "bcbbbcba"
```

**Output:**

```text
4
```

**Explanation:**

The following substring has a length of `4` and contains at most two occurrences of each character:

```text
"bcbb"
```

Therefore, the maximum valid length is:

```text
4
```

---

## Example 2

**Input:**

```text
s = "aaaa"
```

**Output:**

```text
2
```

**Explanation:**

The substring:

```text
"aa"
```

contains exactly two occurrences of `a`.

Any substring longer than `2` would contain more than two occurrences of `a`.

Therefore, the maximum valid length is:

```text
2
```

---

## Approach

Use a **sliding window** with a frequency array.

1. Maintain two pointers, `left` and `right`, representing the current window.
2. Expand the window by moving `right`.
3. Increase the frequency of the current character.
4. If any character occurs more than two times, move `left` forward until the window becomes valid again.
5. Track the maximum valid window length.

This ensures that every character in the current window appears at most twice.

---

## Complexity

### Time Complexity

```text
O(n)
```

Each character is added to and removed from the sliding window at most once.

### Auxiliary Space

```text
O(1)
```

Since the string contains only lowercase English letters, the frequency array has a fixed size of 26.

---

## Constraints

```text
2 <= s.length <= 100
```

`s` consists only of lowercase English letters.
