# Check if Word Sum Equals Target Word

## Problem

The **letter value** of a lowercase letter is its position in the alphabet starting from `0`:

```text
'a' -> 0
'b' -> 1
'c' -> 2
...
'j' -> 9
```

The **numerical value** of a word is obtained by:

1. Replacing each character with its letter value.
2. Concatenating these values into a string.
3. Converting the resulting string into an integer.

Given three strings:

- `firstWord`
- `secondWord`
- `targetWord`

return **true** if:

```text
numericalValue(firstWord) + numericalValue(secondWord)
== numericalValue(targetWord)
```

Otherwise, return **false**.

---

## Examples

### Example 1

**Input**

```text
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
```

**Output**

```text
true
```

**Explanation**

```text
acb -> "021" -> 21
cba -> "210" -> 210
cdb -> "231" -> 231

21 + 210 = 231
```

---

### Example 2

**Input**

```text
firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
```

**Output**

```text
false
```

**Explanation**

```text
aaa -> "000" -> 0
a   -> "0"   -> 0
aab -> "001" -> 1

0 + 0 ≠ 1
```

---

### Example 3

**Input**

```text
firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
```

**Output**

```text
true
```

**Explanation**

```text
aaa  -> "000"  -> 0
a    -> "0"    -> 0
aaaa -> "0000" -> 0

0 + 0 = 0
```

---

## Constraints:

- 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
- firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.

---
