# Water Bottles Problem

## Problem Statement

You have:

- `numBottles` full water bottles  
- You can exchange `numExchange` empty bottles for **1 full bottle**

After drinking a full bottle, it becomes an empty bottle.

Return the **maximum number of bottles you can drink**.

---

## Example 1

**Input**
```
numBottles = 9
numExchange = 3
```

**Output**
```
13
```

**Explanation**

Drink 9 → 9 empty  
Exchange 9/3 = 3 → drink 3 → 3 empty  
Exchange 3/3 = 1 → drink 1  

Total = 9 + 3 + 1 = 13

---

## Example 2

**Input**
```
numBottles = 15
numExchange = 4
```

**Output**
```
19
```

**Explanation**

Drink 15 → 15 empty  
Exchange 15/4 = 3 → drink 3 → total 18  
Now empty = 3 + remainder(3) = 6  
Exchange 6/4 = 1 → drink 1  

Total = 15 + 3 + 1 = 19

---

## Constraints

- 1 <= numBottles <= 100
- 2 <= numExchange <= 100

---
