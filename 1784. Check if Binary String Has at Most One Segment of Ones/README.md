# Check If Binary String Has At Most One Segment of Ones

## Problem Statement

Given a **binary string `s`** without leading zeros, determine whether it contains **at most one contiguous segment of '1's**.

Return:

- `true` → if there is **only one segment of '1's**
- `false` → if there are **multiple separated segments of '1's**

---

## Examples

### Example 1

**Input**
```
s = "1001"
```

**Output**
```
false
```

**Explanation**

There are two segments of `1`:
```
1 00 1
```

So the ones are **not contiguous**.

---

### Example 2

**Input**
```
s = "110"
```

**Output**
```
true
```

**Explanation**

All `1`s appear in **one continuous segment**.

---

## Constraints

- 1 <= s.length <= 100
- s[i] is '0' or '1'
- s[0] = '1'

```
