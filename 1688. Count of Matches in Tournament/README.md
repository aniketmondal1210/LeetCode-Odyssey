# Number of Matches in a Tournament

## Problem Statement
You are given an integer `n`, representing the number of teams in a tournament with the following rules:

- If the number of teams is **even**:
  - Teams are paired.
  - Number of matches played = `n / 2`
  - Teams advancing = `n / 2`

- If the number of teams is **odd**:
  - One team advances automatically.
  - Remaining teams are paired.
  - Number of matches played = `(n - 1) / 2`
  - Teams advancing = `(n - 1) / 2 + 1`

The tournament continues until **one team remains**.

Return the **total number of matches played**.

---

## Examples

### Example 1
**Input:**  

n = 7

**Output:**  

6


**Explanation:**  
- Round 1: 7 teams → 3 matches → 4 teams advance  
- Round 2: 4 teams → 2 matches → 2 teams advance  
- Round 3: 2 teams → 1 match → 1 winner  

Total matches = `3 + 2 + 1 = 6`

---

### Example 2
**Input:**  

n = 14

**Output:**  

13


**Explanation:**  
- Round 1: 14 teams → 7 matches → 7 teams advance  
- Round 2: 7 teams → 3 matches → 4 teams advance  
- Round 3: 4 teams → 2 matches → 2 teams advance  
- Round 4: 2 teams → 1 match → 1 winner  

Total matches = `7 + 3 + 2 + 1 = 13`

---

## Constraints

1 ≤ n ≤ 200

---
