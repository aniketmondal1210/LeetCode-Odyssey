# Replace Words (Prefix Root Replacement)

## Problem Description

In English, we have a concept called a **root**, which can be followed by another word to form a **derivative** (e.g., the root `"help"` followed by `"ful"` forms `"helpful"`).

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the **shortest length**.

Return the sentence after all replacements have been made.

---

## Examples

### Example 1
- **Input:** 
  - `dictionary = ["cat", "bat", "rat"]`
  - `sentence = "the cattle was rattled by the battery"`
- **Output:** `"the cat was rat by the bat"`
- **Explanation:** 
  - `"cattle"` starts with `"cat"` $\rightarrow$ replaced by `"cat"`
  - `"rattled"` starts with `"rat"` $\rightarrow$ replaced by `"rat"`
  - `"battery"` starts with `"bat"` $\rightarrow$ replaced by `"bat"`

### Example 2
- **Input:** 
  - `dictionary = ["a", "b", "c"]`
  - `sentence = "aadsfasf absbs bbab cadsfafs"`
- **Output:** `"a a b c"`

---

## Constraints

- $1 \le \text{dictionary.length} \le 1000$
- $1 \le \text{dictionary}[i].\text{length} \le 100$
- `dictionary[i]` consists of only lowercase English letters.
- $1 \le \text{sentence.length} \le 10^6$
- `sentence` consists of lowercase letters and spaces.
- $1 \le \text{number of words in sentence} \le 1000$
- $1 \le \text{length of each word} \le 1000$
- Every two consecutive words in `sentence` are separated by exactly one space.
- `sentence` does not have leading or trailing spaces.

---
