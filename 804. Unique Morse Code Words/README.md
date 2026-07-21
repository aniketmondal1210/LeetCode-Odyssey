# Unique Morse Code Words

## Problem

International Morse Code assigns each lowercase English letter a unique sequence of dots (`.`) and dashes (`-`).

The Morse code mapping is:

```text
[
".-","-...","-.-.","-..",".","..-.","--.","....","..",
".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
"...","-","..-","...-",".--","-..-","-.--","--.."
]
```

Each word is transformed by concatenating the Morse codes of its letters.

Return the **number of distinct Morse code transformations** among all the given words.

---

## Examples

### Example 1

**Input**

```text
words = ["gin","zen","gig","msg"]
```

**Output**

```text
2
```

**Explanation**

```text
gin -> --...-.
zen -> --...-.
gig -> --...--.
msg -> --...--.
```

Distinct transformations are:

```text
--...-.
--...--.
```

Hence, the answer is **2**.

---

### Example 2

**Input**

```text
words = ["a"]
```

**Output**

```text
1
```

**Explanation**

```text
a -> .-
```

Only one unique transformation exists.

---

## Constraints:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- words[i] consists of lowercase English letters.

---
