# Merge Strings Alternately

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in **alternating order**, starting with `word1`. If one string is longer than the other, append the remaining letters to the end of the merged string.

Return the merged string.

---

## Input

* Two strings `word1` and `word2` consisting of lowercase English letters.

**Constraints:**

```
1 ≤ word1.length, word2.length ≤ 100
```

---

## Output

Return the merged string after combining letters alternately.

---

## Examples

### Example 1

**Input:**

```
word1 = "abc"
word2 = "pqr"
```

**Output:**

```
apbqcr
```

**Explanation:**

```
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

### Example 2

**Input:**

```
word1 = "ab"
word2 = "pqrs"
```

**Output:**

```
apbqrs
```

**Explanation:**

```
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
```

### Example 3

**Input:**

```
word1 = "abcd"
word2 = "pq"
```

**Output:**

```
apbqcd
```

**Explanation:**

```
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
```

---
