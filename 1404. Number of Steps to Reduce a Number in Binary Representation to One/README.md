# Number of Steps to Reduce Binary String to 1

## Problem Summary

Given a binary string `s`, reduce it to `"1"` using:

- If even → divide by 2  
- If odd → add 1  

Return the total number of steps required.

---

---

## Example

### Input 1
```
s = "1101"
```

### Output
```
6
```

## Explanation: 
```
"1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.
```


### Input 2
```
s = "10"
```

### Output
```
1
```

## Explanation: 
```
"10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.
```


### Input 1
```
s = "1"
```

### Output
```
0
```

### Constraints:

- 1 <= s.length <= 500
- s consists of characters '0' or '1'
- s[0] == '1'

---
