# Sort Integers by Number of 1 Bits

## Problem Statement

Given an array `arr`, sort it based on:

1. **Number of 1's (set bits)** in binary representation (ascending)
2. If tie → sort by **value (ascending)**

---

# Examples

### Example 1

**Input**
```
arr = [0,1,2,3,4,5,6,7,8]
```

**Binary + Set Bits**
```
0 → 0000 → 0 bits
1 → 0001 → 1 bit
2 → 0010 → 1 bit
3 → 0011 → 2 bits
4 → 0100 → 1 bit
5 → 0101 → 2 bits
6 → 0110 → 2 bits
7 → 0111 → 3 bits
8 → 1000 → 1 bit
```

**Sorted**
```
[0,1,2,4,8,3,5,6,7]
```

---

### Example 2

**Input**
```
arr = [1024,512,256,128,64,32,16,8,4,2,1]
```

All have **1 set bit**, so sort normally:

```
[1,2,4,8,16,32,64,128,256,512,1024]
```

---

## Constraints:

- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^4

---
