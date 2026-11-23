# Share the Umbrella

## Problem Description

You are given a binary array `rain` of length `n`, where `rain[i] == 1` indicates rain on day `i` and `rain[i] == 0` indicates no rain.

Alice and Bob share a single umbrella over `n` days with the following rules on each day `i` (`0 <= i < n`):
- Alice needs the umbrella if `i + 1 < n` and `rain[i] == 1` and `rain[i + 1] == 1`.
- Bob needs the umbrella if `rain[i] == 1`.
- If neither needs it, the assignment is `"None"`.
- If only one person needs it, that person receives it.
- If both need it, whoever has received the umbrella fewer times so far receives it; if tied (`alice_count == bob_count`), Alice receives it.
- A person's count increments only on a day they receive the umbrella, starting at `0` for both.

Return a list/array `answer` of length `n` containing `"Alice"`, `"Bob"`, or `"None"` for each day.

---

## Examples

### Example 1
- **Input:** `rain = [1, 1, 0, 1, 1]`
- **Output:** `["Alice", "Bob", "None", "Alice", "Bob"]`
- **Explanation:**
  - Day `0`: Both need it; counts are tied at `0`, so `"Alice"` gets it (`alice_count = 1`).
  - Day `1`: Only `"Bob"` needs it (`bob_count = 1`).
  - Day `2`: Neither needs it (`"None"`).
  - Day `3`: Both need it; counts are tied at `1`, so `"Alice"` gets it (`alice_count = 2`).
  - Day `4`: Last day, so only `"Bob"` needs it (`bob_count = 2`).

### Example 2
- **Input:** `rain = [0, 1, 0, 1]`
- **Output:** `["None", "Bob", "None", "Bob"]`
- **Explanation:** Rain never occurs on two consecutive days, so Alice never needs the umbrella. Bob receives it on days `1` and `3`, while days `0` and `2` are `"None"`.

---

## Constraints

- $1 \le n = \text{rain.length} \le 100$
- `rain[i]` is either `0` or `1`.

---
