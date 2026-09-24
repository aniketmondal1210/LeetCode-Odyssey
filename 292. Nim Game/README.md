# Nim Game

## Problem Description

You are playing the following **Nim Game** with a friend:
- Initially, there is a heap of $n$ stones on the table.
- You and your friend alternate taking turns, and **you go first**.
- On each turn, the player whose turn it is can remove **1, 2, or 3 stones** from the heap.
- The player who removes the last stone wins the game.

Given $n$, the number of stones in the heap, return `true` if you can win the game assuming both you and your friend play optimally, otherwise return `false`.

---

## Examples

### Example 1
- **Input:** `n = 4`
- **Output:** `false`
- **Explanation:** 
  - If you remove 1 stone, 3 remain. Your friend removes 3 stones and wins.
  - If you remove 2 stones, 2 remain. Your friend removes 2 stones and wins.
  - If you remove 3 stones, 1 remains. Your friend removes 1 stone and wins.
  In all cases, your friend wins.

### Example 2
- **Input:** `n = 1`
- **Output:** `true`
- **Explanation:** You remove 1 stone and win immediately.

### Example 3
- **Input:** `n = 2`
- **Output:** `true`
- **Explanation:** You remove 2 stones and win immediately.

---

## Constraints

- $1 \le n \le 2^{31} - 1$

---
