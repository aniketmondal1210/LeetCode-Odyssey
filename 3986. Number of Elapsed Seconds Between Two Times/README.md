# Calculate Elapsed Seconds Between Two Times

## Problem

You are given two valid times `startTime` and `endTime`, each represented as a string in the format:

```text
"HH:MM:SS"
```

Return the number of **seconds that have elapsed** from `startTime` to `endTime`.

---

## Examples

### Example 1

**Input**

```text
startTime = "01:00:00"
endTime = "01:00:25"
```

**Output**

```text
25
```

**Explanation**

`endTime` is **25 seconds** ahead of `startTime`.

---

### Example 2

**Input**

```text
startTime = "12:34:56"
endTime = "13:00:00"
```

**Output**

```text
1504
```

**Explanation**

The elapsed time is:

- 25 minutes = 1500 seconds
- 4 seconds

Total:

```text
1500 + 4 = 1504 seconds
```

---

## Constraints:

- startTime.length == 8
- endTime.length == 8
- startTime and endTime are valid times in the format "HH:MM:SS"
- 00 <= HH <= 23
- 00 <= MM <= 59
- 00 <= SS <= 59
- endTime is not earlier than startTime

---
