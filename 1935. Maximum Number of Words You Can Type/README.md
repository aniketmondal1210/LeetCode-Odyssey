# Count Typable Words with Broken Keyboard

## Problem Statement
There is a malfunctioning keyboard where some letter keys do not work.  
All other keys work properly.

You are given:
- A string `text` consisting of words separated by a single space (no leading or trailing spaces).
- A string `brokenLetters` containing all distinct broken keys.

Your task is to return the **number of words in `text`** that can be fully typed using this keyboard.

---

## Examples

**Example 1:**

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: "world" cannot be typed because 'd' is broken.


**Example 2:**

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: "leet" cannot be typed because 'l' and 't' are broken.


**Example 3:**

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: Neither word can be typed because 'e' is broken.


---

## Constraints
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space (no leading or trailing spaces).
- Each word consists only of lowercase English letters.
- `brokenLetters` contains distinct lowercase English letters.

---
