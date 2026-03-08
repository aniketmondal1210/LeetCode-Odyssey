# Find Box with Minimum Capacity to Store Item

## Problem Statement

You are given:

- An integer array `capacity[]`, where `capacity[i]` represents the capacity of the **i-th box**.
- An integer `itemSize` representing the size of an item.

A box can store the item if:

```
capacity[i] >= itemSize
```

Return the **index of the box with the minimum capacity that can store the item**.

If multiple boxes have the same minimum capacity, return the **smallest index**.

If no box can store the item, return:

```
-1
```

---

## Examples

### Example 1

**Input**
```
capacity = [1,5,3,7]
itemSize = 3
```

**Output**
```
2
```

**Explanation**

Boxes that can store the item:

```
index 1 → capacity 5
index 2 → capacity 3
index 3 → capacity 7
```

Minimum valid capacity = **3** → index **2**

---

### Example 2

**Input**
```
capacity = [3,5,4,3]
itemSize = 2
```

**Output**
```
0
```

**Explanation**

Valid capacities:

```
3,5,4,3
```

Minimum capacity = **3**

Indices with capacity 3:

```
0, 3
```

Return **smallest index = 0**

---

### Example 3

**Input**
```
capacity = [4]
itemSize = 5
```

**Output**
```
-1
```

**Explanation**

No box has capacity ≥ 5.

---

## Constraints:

- 1 <= capacity.length <= 100
- 1 <= capacity[i] <= 100
- 1 <= itemSize <= 100©

---
