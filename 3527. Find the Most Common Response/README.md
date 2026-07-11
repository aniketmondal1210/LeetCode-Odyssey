# Find the Most Common Survey Response

## Problem

You are given a 2D string array `responses`, where `responses[i]` contains the survey responses from the **i-th day**.

Before counting frequencies, remove **duplicate responses within each day**.

Return:

- The response that appears on the **most days**.
- If multiple responses have the same highest frequency, return the **lexicographically smallest** one.

---

## Examples

### Example 1

**Input**

```text
responses = [
  ["good","ok","good","ok"],
  ["ok","bad","good","ok","ok"],
  ["good"],
  ["bad"]
]
```

**Output**

```text
"good"
```

**Explanation**

After removing duplicates from each day:

```text
[
  ["good","ok"],
  ["ok","bad","good"],
  ["good"],
  ["bad"]
]
```

Frequencies become:

```text
good -> 3
ok   -> 2
bad  -> 2
```

Since `"good"` has the highest frequency, return `"good"`.

---

### Example 2

**Input**

```text
responses = [
  ["good","ok","good"],
  ["ok","bad"],
  ["bad","notsure"],
  ["great","good"]
]
```

**Output**

```text
"bad"
```

**Explanation**

After removing duplicates:

```text
[
  ["good","ok"],
  ["ok","bad"],
  ["bad","notsure"],
  ["great","good"]
]
```

Frequencies:

```text
bad     -> 2
good    -> 2
ok      -> 2
great   -> 1
notsure -> 1
```

There is a tie between `"bad"`, `"good"`, and `"ok"`.

The lexicographically smallest string is `"bad"`.

---

## Constraints:

- 1 <= responses.length <= 1000
- 1 <= responses[i].length <= 1000
- 1 <= responses[i][j].length <= 10
- responses[i][j] consists of only lowercase English letters

---
