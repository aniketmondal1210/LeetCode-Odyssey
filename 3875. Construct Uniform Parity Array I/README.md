# Make Array Parity Same

## Problem Description

You are given an array `nums1` of $n$ distinct integers.

You want to construct another array `nums2` of length $n$ such that the elements in `nums2` are either **all odd** or **all even**.

For each index $i$, you must choose exactly one of the following operations:
- $\text{nums2}[i] = \text{nums1}[i]$
- $\text{nums2}[i] = \text{nums1}[i] - \text{nums1}[j]$, for some index $j \neq i$

Return `true` if it is possible to construct such an array `nums2`, otherwise return `false`.

---

## Examples

### Example 1
- **Input:** `nums1 = [2, 3]`
- **Output:** `true`
- **Explanation:**
  - Choose $\text{nums2}[0] = \text{nums1}[0] - \text{nums1}[1] = 2 - 3 = -1$ (Odd)
  - Choose $\text{nums2}[1] = \text{nums1}[1] = 3$ (Odd)
  - $\text{nums2} = [-1, 3]$ (All elements are odd). Return `true`.

### Example 2
- **Input:** `nums1 = [4, 6]`
- **Output:** `true`
- **Explanation:**
  - Choose $\text{nums2}[0] = \text{nums1}[0] = 4$ (Even)
  - Choose $\text{nums2}[1] = \text{nums1}[1] = 6$ (Even)
  - $\text{nums2} = [4, 6]$ (All elements are even). Return `true`.

---

## Constraints

- $1 \le n = \text{nums1.length} \le 100$
- $1 \le \text{nums1}[i] \le 100$
- `nums1` consists of distinct integers.

---

## Parity Operations Logic

Understanding how parity changes under subtraction:

| Left Operand | Right Operand | Resulting Parity | Formula |
| :--- | :--- | :--- | :--- |
| **Even** | **Even** | **Even** | $\text{Even} - \text{Even} = \text{Even}$ |
| **Odd** | **Odd** | **Even** | $\text{Odd} - \text{Odd} = \text{Even}$ |
| **Even** | **Odd** | **Odd** | $\text{Even} - \text{Odd} = \text{Odd}$ |
| **Odd** | **Even** | **Odd** | $\text{Odd} - \text{Even} = \text{Odd}$ |

---

## Strategy & Analysis

1. **Making All Elements Even:**
   - **Case A:** If all elements are already even, keep them as-is.
   - **Case B:** If there are at least **two odd elements**, subtract another odd element from each odd element to turn them all into even numbers.

2. **Making All Elements Odd:**
   - **Case A:** If all elements are already odd, keep them as-is.
   - **Case B:** If there is at least **one odd element**, subtract that odd element from every even element to make all even elements odd while keeping the odd element as-is.

Since every valid array either has no odd elements, at least two odd elements, or exactly one odd element (where all even elements can be subtracted by that odd element), **it is always mathematically possible to make all elements either all odd or all even**.

Thus, the function can directly return `true` for all valid inputs.

---

## Mathematical Summary

- **Time Complexity:** $\mathcal{O}(1)$ — constant time.
- **Space Complexity:** $\mathcal{O}(1)$ — constant auxiliary space.

---

## Code Implementations

### Python 3

```python
def canMakeSameParity(nums1: list[int]) -> bool:
    # Always possible given the problem constraints
    return True

# Test Cases
if __name__ == "__main__":
    print(canMakeSameParity([2, 3]))  # True
    print(canMakeSameParity([4, 6]))  # True
```

---

### C++

```cpp
#include <iostream>
#include <vector>

bool canMakeSameParity(const std::vector<int>& nums1) {
    return true;
}

int main() {
    std::cout << std::boolalpha;
    std::cout << canMakeSameParity({2, 3}) << std::endl; // true
    std::cout << canMakeSameParity({4, 6}) << std::endl; // true
    return 0;
}
```

---

### Java

```java
public class MakeArrayParitySame {
    public static boolean canMakeSameParity(int[] nums1) {
        return true;
    }

    public static void main(String[] args) {
        System.out.println(canMakeSameParity(new int[]{2, 3})); // true
        System.out.println(canMakeSameParity(new int[]{4, 6})); // true
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
