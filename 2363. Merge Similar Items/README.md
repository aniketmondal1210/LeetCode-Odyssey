# Merge Similar Items

## Problem

You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items.

Each item is represented as:

```text
[value, weight]
```

The `value` of each item is unique within each array.

Return a 2D integer array `ret` where each entry is:

```text
[value, totalWeight]
```

where `totalWeight` is the sum of the weights of all items having that value across both arrays.

The result must be sorted in **ascending order by value**.

## Examples

### Example 1

**Input:**

```text
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
```

**Output:**

```text
[[1,6],[3,9],[4,5]]
```

### Example 2

**Input:**

```text
items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]
```

**Output:**

```text
[[1,4],[2,4],[3,4]]
```

### Example 3

**Input:**

```text
items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
```

**Output:**

```text
[[1,7],[2,4],[7,1]]
```

## Constraints

- `1 <= items1.length, items2.length <= 1000`
- `items1[i].length == items2[i].length == 2`
- `1 <= valuei, weighti <= 1000`
- Each `valuei` in `items1` is unique.
- Each `valuei` in `items2` is unique.
