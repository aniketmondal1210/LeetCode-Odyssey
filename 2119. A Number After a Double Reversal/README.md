# Double Reversal Check

## Problem Statement

Reversing an integer means to reverse all its digits.

For example, reversing `2021` gives `1202`. Reversing `12300` gives `321` as the leading zeros are not retained.

Given an integer `num`, reverse `num` to get `reversed1`, then reverse `reversed1` to get `reversed2`.

Return `true` if `reversed2` equals `num`. Otherwise return `false`.

---

## Examples

**Example 1:**

Input:  
`num = 526`  
Output:  
`true`  
Explanation: Reverse 526 → 625 → 526. So, result is `true`.

---

**Example 2:**

Input:  
`num = 1800`  
Output:  
`false`  
Explanation: Reverse 1800 → 81 → 18 ≠ 1800. So, result is `false`.

---

**Example 3:**

Input:  
`num = 0`  
Output:  
`true`  
Explanation: Reverse 0 → 0 → 0. So, result is `true`.

---

## Constraints

- `0 <= num <= 10^6`
