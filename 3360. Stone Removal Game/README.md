# Stone Removal Game

## Problem Description

Alice and Bob play a turn-based game with a pile of `n` stones, with Alice moving first:
- On her first turn, Alice removes **exactly `10` stones**.
- On every subsequent turn, the current player removes **exactly `1` fewer stone** than the previous player removed.
- The first player unable to remove the required number of stones loses.

Given a positive integer `n`, return `true` if Alice wins the game and `false` otherwise.

---

## Examples

### Example 1
- **Input:** `n = 12`
- **Output:** `true`
- **Explanation:** Alice removes `10` stones on turn 1 (`2` stones remain). Bob needs to remove `9` stones on turn 2, which is impossible (`2 < 9`), so Alice wins.

### Example 2
- **Input:** `n = 1`
- **Output:** `false`
- **Explanation:** Alice cannot remove `10` stones on her first turn (`1 < 10`), so Alice loses immediately.

---

## Constraints

- $1 \le n \le 50$

---
