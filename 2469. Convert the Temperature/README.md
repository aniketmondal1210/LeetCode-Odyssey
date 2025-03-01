# Problem: Convert Celsius to Kelvin and Fahrenheit

## Problem Statement
Given a non-negative floating point number `celsius` rounded to two decimal places, return an array `ans = [kelvin, fahrenheit]`, where:
- `kelvin = celsius + 273.15`
- `fahrenheit = celsius * 1.80 + 32.00`

Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `0 <= celsius <= 1000`

## Examples
### Example 1
- **Input:** `celsius = 36.50`
- **Output:** `[309.65000, 97.70000]`
- **Explanation:**  
  - `Kelvin = 36.50 + 273.15 = 309.65`  
  - `Fahrenheit = 36.50 * 1.80 + 32.00 = 97.70`  

### Example 2
- **Input:** `celsius = 122.11`
- **Output:** `[395.26000, 251.79800]`
- **Explanation:**  
  - `Kelvin = 122.11 + 273.15 = 395.26`  
  - `Fahrenheit = 122.11 * 1.80 + 32.00 = 251.798`
