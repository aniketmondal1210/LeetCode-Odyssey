# Implement `Array.prototype.groupBy(fn)`

## Problem Statement

Enhance all arrays such that you can call the method `array.groupBy(fn)` on any array.  
This method should return an **object** where:
- Each **key** is the result of applying `fn` to an array element.
- Each **value** is an array of all elements that produced that key.

---

## Example 1

**Input:**

array = [
  {"id": "1"},
  
  {"id": "1"},
  
  {"id": "2"}
];

fn = function (item) { 

  return item.id; 
}

**Output:**

{ 
  "1": [{"id": "1"}, {"id": "1"}],
  
  "2": [{"id": "2"}]
}

Explanation:

Two elements have id = 1, one has id = 2.

They are grouped based on their id values.

**Example 2**

**Input:**

array = [
  [1, 2, 3],
  
  [1, 3, 5],
  
  [1, 5, 9]
];
fn = function (list) { 

  return String(list[0]); 
}

**Output:**

{ 
  "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]] 
}

Explanation:

The key is the first element of each list.

Since all lists start with 1, all are grouped under "1".

## Example 3

**Input:**

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
fn = function (n) { 
  return String(n > 5);
}

**Output:**

{
  "true": [6, 7, 8, 9, 10],
  
  "false": [1, 2, 3, 4, 5]
}

Explanation:

Numbers are grouped by whether they are greater than 5.

## Constraints

- 0 <= array.length <= 10^5
- fn returns a string

Expected Time Complexity: O(N)

Expected Space Complexity: O(N)
