# Find the Number of Possible Original Strings

## Problem

Alice intended to type a string but may have accidentally **held down a key once**, causing **one character** to be typed multiple times consecutively.

You are given the final string `word` displayed on the screen.

Return the total number of possible original strings Alice might have intended to type.

> Alice could have:
>
> - Never held a key (the original string is `word` itself), or
> - Held **exactly one** key, causing one consecutive group of identical characters to become longer.

---

## Examples

### Example 1

**Input**

```text
word = "abbcccc"
```

**Output**

```text
5
```

**Explanation**

The consecutive groups are:

```text
a
bb
cccc
```

Possible original strings are:

```text
abbcccc
abbccc
abbcc
abbc
abcccc
```

Total = **5**

---

### Example 2

**Input**

```text
word = "abcd"
```

**Output**

```text
1
```

**Explanation**

Every character appears only once, so no long press could have occurred.

Only possible original string:

```text
abcd
```

---

### Example 3

**Input**

```text
word = "aaaa"
```

**Output**

```text
4
```

**Explanation**

The only group has length 4.

Possible originals:

```text
aaaa
aaa
aa
a
```

Total = **4**

---

## Constraints:

- 1 <= word.length <= 100
- word consists only of lowercase English letters.

---
