# Train Arrival Time After Delay

## Problem Statement

You are given a positive integer `arrivalTime` denoting the arrival time of a train in hours (24-hour format), and another positive integer `delayedTime` denoting the amount of delay in hours.

Return the time when the train will **actually arrive** at the station after the delay.

---

## Examples

### Example 1  
**Input:**  
`arrivalTime = 15`, `delayedTime = 5`  
**Output:**  
`20`  
**Explanation:**  
Arrival time was 15:00. With a 5-hour delay, the new arrival time is `15 + 5 = 20`.

---

### Example 2  
**Input:**  
`arrivalTime = 13`, `delayedTime = 11`  
**Output:**  
`0`  
**Explanation:**  
Arrival time was 13:00. With an 11-hour delay, the new arrival time is `13 + 11 = 24`, which is `0` in 24-hour format.

---

## Constraints

- `1 <= arrivalTime < 24`
- `1 <= delayedTime <= 24`

---
