# Decode the Message

## Problem Statement

You are given two strings:

- `key` — a cipher key containing lowercase English letters and spaces.
- `message` — the secret message to decode.

The decoding process works as follows:

1. Traverse `key` from left to right.
2. Take the **first appearance** of each lowercase English letter.
3. This creates a substitution table containing all 26 letters.
4. Align this table with the normal alphabet:

```text
Normal:       a b c d e f g h i j k l m n o p q r s t u v w x y z
Substitution: ...
```

5. For every character in `message`, replace it using the substitution table.
6. Spaces remain unchanged.

Return the decoded message.

---

## Examples

### Example 1

**Input**

```text
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
```

**Output**

```text
"this is a secret"
```

**Explanation**

The first appearances of the letters in `key` form the substitution order:

```text
t h e q u i c k b r o w n f x j m p s v l a z y d g
```

Aligning this with the normal alphabet gives mappings such as:

```text
t -> a
h -> b
e -> c
q -> d
u -> e
i -> f
...
```

Using this mapping, `"vkbs bs t suepuv"` becomes:

```text
"this is a secret"
```

---

### Example 2

**Input**

```text
key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
```

**Output**

```text
"the five boxing wizards jump quickly"
```

---

## Constraints:

- 26 <= key.length <= 2000
- key consists of lowercase English letters and ' '.
- key contains every letter in the English alphabet ('a' to 'z') at least once.
- 1 <= message.length <= 2000
- message consists of lowercase English letters and ' '.

---
