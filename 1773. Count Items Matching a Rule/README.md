# Count Items Matching a Rule

## Problem Statement

You are given a 2D array `items`, where:
```
items[i] = [typei, colori, namei]
```

You are also given:
- `ruleKey` → one of `"type"`, `"color"`, `"name"`
- `ruleValue`

👉 Count how many items match the rule.

---

## Matching Condition

An item matches if:

```
ruleKey == "type"  → typei == ruleValue
ruleKey == "color" → colori == ruleValue
ruleKey == "name"  → namei == ruleValue
```

---

# Examples

### Example 1

**Input**
```
items = [["phone","blue","pixel"],
         ["computer","silver","lenovo"],
         ["phone","gold","iphone"]]

ruleKey = "color"
ruleValue = "silver"
```

**Output**
```
1
```

---

### Example 2

**Input**
```
items = [["phone","blue","pixel"],
         ["computer","silver","phone"],
         ["phone","gold","iphone"]]

ruleKey = "type"
ruleValue = "phone"
```

**Output**
```
2
```

---

## Constraints:

- 1 <= items.length <= 10^4
- 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
- ruleKey is equal to either "type", "color", or "name".
- All strings consist only of lowercase letters.

---
