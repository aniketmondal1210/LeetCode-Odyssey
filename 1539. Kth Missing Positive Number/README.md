# Kth Missing Positive Number

## Problem Statement

Given a **sorted strictly increasing array** `arr` and an integer `k`, return the **kth missing positive integer**.

---

# Examples

### Example 1

**Input**
```
arr = [2,3,4,7,11], k = 5
```

**Missing Numbers**
```
[1,5,6,8,9,10,12,...]
```

**5th missing →**
```
9
```

**Output**
```
9
```

---

### Example 2

**Input**
```
arr = [1,2,3,4], k = 2
```

**Missing Numbers**
```
[5,6,7,...]
```

**2nd missing →**
```
6
```

**Output**
```
6
```

---

## Constraints:

- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
- 1 <= k <= 1000
- arr[i] < arr[j] for 1 <= i < j <= arr.length
 

## Follow up:

- Could you solve this problem in less than O(n) complexity?

---
