# Problem: Remove Anagrams

## Problem Statement

You are given a **0-indexed** string array `words`, where `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that:

```text
0 < i < words.length
```

and `words[i - 1]` and `words[i]` are **anagrams**. Then delete `words[i]` from `words`.

Keep performing this operation as long as you can select an index that satisfies the conditions.

Return `words` after performing all operations.

It can be shown that selecting the indices for each operation in **any** arbitrary order will lead to the same result.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once.

For example:

```text
"dacb" is an anagram of "abdc"
```

---

## Example 1

**Input:**

```text
words = ["abba", "baba", "bbaa", "cd", "cd"]
```

**Output:**

```text
["abba", "cd"]
```

**Explanation:**

One of the ways to obtain the resultant array is:

1. `words[2] = "bbaa"` and `words[1] = "baba"` are anagrams, so delete `words[2]`.

```text
["abba", "baba", "cd", "cd"]
```

2. `words[1] = "baba"` and `words[0] = "abba"` are anagrams, so delete `words[1]`.

```text
["abba", "cd", "cd"]
```

3. `words[2] = "cd"` and `words[1] = "cd"` are anagrams, so delete `words[2]`.

```text
["abba", "cd"]
```

No more operations can be performed, so the final answer is:

```text
["abba", "cd"]
```

---

## Example 2

**Input:**

```text
words = ["a", "b", "c", "d", "e"]
```

**Output:**

```text
["a", "b", "c", "d", "e"]
```

**Explanation:**

No two adjacent strings in `words` are anagrams of each other, so no operations are performed.

Therefore, the original array remains unchanged.

---

## Constraints

```text
1 <= words.length <= 100
1 <= words[i].length <= 10
```

`words[i]` consists only of lowercase English letters.
