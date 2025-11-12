# Merge Two Arrays of Objects by `id`

## Problem Statement

Given two arrays `arr1` and `arr2`, return a new array `joinedArray`.  

Each object in both arrays contains an `id` field (an integer).

The `joinedArray` is formed by merging `arr1` and `arr2` **based on their `id`**.

### Rules:
1. The result must contain **unique ids** only.
2. The result must be **sorted in ascending order of id**.
3. If an `id` appears in only one array → include that object as-is.
4. If an `id` appears in both arrays → merge their properties:
   - Keys that exist in only one object should remain.
   - Keys that exist in both → **value from `arr2` overrides** the value from `arr1`.

---

## Example 1

**Input:**
arr1 = [

  { "id": 1, "x": 1 },
  
  { "id": 2, "x": 9 }

  
];

arr2 = [

  { "id": 3, "x": 5 }

];

Output:

[

  { "id": 1, "x": 1 },
  
  { "id": 2, "x": 9 },
  
  { "id": 3, "x": 5 }

]

Explanation:

No duplicate ids, so we simply combine both arrays.

Example 2

Input:

arr1 = [

  { "id": 1, "x": 2, "y": 3 },
  
  { "id": 2, "x": 3, "y": 6 }

];

arr2 = [

  { "id": 2, "x": 10, "y": 20 },
  
  { "id": 3, "x": 0, "y": 0 }

];

Output:

[

  { "id": 1, "x": 2, "y": 3 },
  
  { "id": 2, "x": 10, "y": 20 },
  
  { "id": 3, "x": 0, "y": 0 }

]

Explanation:

    id=1 and id=3 appear once → added directly.

    id=2 appears in both → merged with arr2 values overriding arr1.

Example 3

Input:

arr1 = [
 
  { "id": 1, "b": { "b": 94 }, "v": [4, 3], "y": 48 }

];

arr2 = [
 
  { "id": 1, "b": { "c": 84 }, "v": [1, 3] }

];

Output:

[

  { "id": 1, "b": { "c": 84 }, "v": [1, 3], "y": 48 }

]

Explanation:

    Keys b and v exist in both objects → arr2 overrides.

    Key y exists only in arr1 → preserved.

Constraints

- Each object has a unique integer `id` within its array.
- 2 ≤ JSON.stringify(arr1).length ≤ 10⁶
- 2 ≤ JSON.stringify(arr2).length ≤ 10⁶
