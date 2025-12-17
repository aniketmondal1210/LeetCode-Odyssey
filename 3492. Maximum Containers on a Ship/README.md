# Maximum Containers on a Ship

## Problem Statement
You are given a positive integer `n` representing an **n × n cargo deck** on a ship.  
Each cell of the deck can hold **one container**, and each container has a fixed weight `w`.

The **total weight** of all containers loaded onto the deck must **not exceed** the ship’s maximum weight capacity `maxWeight`.

Your task is to return the **maximum number of containers** that can be loaded onto the ship.

---

## Example 1

### Input

n = 2
w = 3
maxWeight = 15


### Output

4


### Explanation
- Total deck cells = 2 × 2 = 4  
- Weight if all containers are loaded = 4 × 3 = 12  
- Since 12 ≤ 15, all 4 containers can be loaded.

---

## Example 2

### Input

n = 3
w = 5
maxWeight = 20


### Output

4


### Explanation
- Total deck cells = 3 × 3 = 9  
- Each container weighs 5  
- Maximum containers without exceeding capacity = ⌊20 / 5⌋ = 4  
- Only 4 containers can be loaded even though there are 9 cells.

---

### Constraints

- 1 ≤ n ≤ 1000
- 1 ≤ w ≤ 1000
- 1 ≤ maxWeight ≤ 10⁹

---
