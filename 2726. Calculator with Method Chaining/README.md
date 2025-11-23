# Implement a Chainable Calculator Class

## Requirements

Design a **Calculator** class with method chaining support.  
The constructor accepts an initial number (`result`), and each operation updates this result.

### Methods

1. **add(value)**  
   Adds `value` to `result`. Returns the Calculator instance.

2. **subtract(value)**  
   Subtracts `value` from `result`. Returns the Calculator instance.

3. **multiply(value)**  
   Multiplies `result` by `value`. Returns the Calculator instance.

4. **divide(value)**  
   Divides `result` by `value`.  
   If `value == 0`, throw error:  
   `"Division by zero is not allowed"`

5. **power(value)**  
   Raises `result` to the power `value`. Returns the Calculator instance.

6. **getResult()**  
   Returns the current result.

All results within **1e-5** of expected values are accepted.

---

## Example 1
**Input**

actions = ["Calculator", "add", "subtract", "getResult"]
values = [10, 5, 7]


**Output**

8


**Explanation**

new Calculator(10).add(5).subtract(7).getResult();


---

## Example 2
**Input**

actions = ["Calculator", "multiply", "power", "getResult"]
values = [2, 5, 2]


**Output**

100


---

## Example 3
**Input**

actions = ["Calculator", "divide", "getResult"]
values = [20, 0]


**Output**

"Division by zero is not allowed"


---
