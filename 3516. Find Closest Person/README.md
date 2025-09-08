# Who Reaches Person 3 First?

You are given three integers `x`, `y`, and `z`, representing the positions of three people on a number line:

- `x` → position of **Person 1**
- `y` → position of **Person 2**
- `z` → position of **Person 3** (who does not move)

Both Person 1 and Person 2 move toward Person 3 at the same speed.

## Task
Determine which person reaches Person 3 first:

- Return **1** if Person 1 arrives first.  
- Return **2** if Person 2 arrives first.  
- Return **0** if both arrive at the same time.  

---

## Examples

### Example 1
**Input:**  

x = 2, y = 7, z = 4


**Output:**  

1


**Explanation:**  
- Person 1 → |2 - 4| = 2 steps  
- Person 2 → |7 - 4| = 3 steps  
Since Person 1 is closer, output = **1**.

---

### Example 2
**Input:**  

x = 2, y = 5, z = 6


**Output:**  

2


**Explanation:**  
- Person 1 → |2 - 6| = 4 steps  
- Person 2 → |5 - 6| = 1 step  
Since Person 2 is closer, output = **2**.

---

### Example 3
**Input:**  

x = 1, y = 5, z = 3


**Output:**  

0


**Explanation:**  
- Person 1 → |1 - 3| = 2 steps  
- Person 2 → |5 - 3| = 2 steps  
Both take the same time, output = **0**.

---

## Constraints
- 1 <= x, y, z <= 100  

---
