# Weighted Word Mapping

## Problem Statement

You are given:

- An array of strings `words`
- An integer array `weights` of size `26`

where:

```text
weights[i]
```

represents the weight of the `i-th` lowercase English letter.

---

## Word Weight

The weight of a word is:

```text
sum of weights of all its characters
```

After calculating the word weight:

```text
weight % 26
```

Map the result using **reverse alphabetical order**:

```text
0  -> 'z'
1  -> 'y'
2  -> 'x'
...
25 -> 'a'
```

Return the final string formed by concatenating all mapped characters.

---

# Examples

### Example 1

```text
Input:
words = ["abcd","def","xyz"]

weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

Output:
"rij"
```

---

### Explanation

#### Word `"abcd"`

```text
a = 5
b = 3
c = 12
d = 14

Total = 34
34 % 26 = 8
```

Mapping:

```text
8 -> 'r'
```

---

#### Word `"def"`

```text
14 + 1 + 2 = 17
17 % 26 = 17
```

Mapping:

```text
17 -> 'i'
```

---

#### Word `"xyz"`

```text
7 + 7 + 2 = 16
16 % 26 = 16
```

Mapping:

```text
16 -> 'j'
```

Final Answer:

```text
"rij"
```

---

# Constraints

```text
1 <= words.length <= 100
1 <= words[i].length <= 10
weights.length == 26
1 <= weights[i] <= 100
```

---
