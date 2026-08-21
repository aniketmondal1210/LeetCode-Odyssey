# Complex Number Multiplication

## Problem

A complex number can be represented as a string in the form `"real+imaginaryi"` where:

- `real` is the real part and is an integer in the range `[-100, 100]`.
- `imaginary` is the imaginary part and is an integer in the range `[-100, 100]`.
- `i² = -1`.

Given two complex numbers `num1` and `num2` as strings, return a string representing their multiplication.

## Examples

### Example 1

```text
Input:
num1 = "1+1i"
num2 = "1+1i"

Output:
"0+2i"
```

**Explanation:**

```text
(1 + i) * (1 + i)
= 1 + i² + 2i
= 2i
```

Therefore, the result is represented as `"0+2i"`.

### Example 2

```text
Input:
num1 = "1+-1i"
num2 = "1+-1i"

Output:
"0+-2i"
```

**Explanation:**

```text
(1 - i) * (1 - i)
= 1 + i² - 2i
= -2i
```

Therefore, the result is represented as `"0+-2i"`.

## Constraints

- `num1` and `num2` are valid complex numbers.
