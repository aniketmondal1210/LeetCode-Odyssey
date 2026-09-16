# Finding Distinct 3-Digit Even Numbers

## Problem Description

You are given an array of digits called `digits`. Your task is to determine the number of distinct **three-digit even numbers** that can be formed using these digits.

> **Note:**
> - Each copy of a digit can only be used once per formed number.
> - The formed number cannot have leading zeros (i.e., it must be in the range $[100, 999]$).

---

## Examples

### Example 1
- **Input:** `digits = [1, 2, 3, 4]`
- **Output:** `12`
- **Explanation:** The 12 distinct 3-digit even numbers that can be formed are:
  `124`, `132`, `134`, `142`, `214`, `234`, `312`, `314`, `324`, `342`, `412`, and `432`.
  *(Note that `222` cannot be formed because there is only 1 copy of digit `2`)*.

### Example 2
- **Input:** `digits = [0, 2, 2]`
- **Output:** `2`
- **Explanation:** The only 3-digit even numbers that can be formed are `202` and `220`.

### Example 3
- **Input:** `digits = [6, 6, 6]`
- **Output:** `1`
- **Explanation:** Only `666` can be formed.

### Example 4
- **Input:** `digits = [1, 3, 5]`
- **Output:** `0`
- **Explanation:** No even 3-digit numbers can be formed.

---

## Constraints

- $3 \le \text{digits.length} \le 10$
- $0 \le \text{digits}[i] \le 9$

---

## Approach & Algorithm

Instead of generating all permutations of 3 digits from the given array, we can invert the search space:

1. **Frequency Count:** Count the frequency of each digit ($0$ through $9$) present in the input array `digits`.
2. **Iterate Target Range:** Loop through all candidate 3-digit even numbers, which strictly range from `100` to `998` with a step of `2`.
3. **Validate Digits:**
   - Extract the hundreds ($d_1$), tens ($d_2$), and units ($d_3$) digits for each candidate number.
   - Count the required frequency of each digit used by the candidate number.
   - Check if our input array `digits` contains **at least** as many copies of each digit as required.
4. **Count:** If valid, increment our total count of valid distinct numbers.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ — The loop runs a fixed number of times ($450$ iterations, from $100$ to $998$ step $2$). Counting array frequencies takes $\mathcal{O}(N)$ where $N \le 10$, so the runtime is constant.
- **Space Complexity:** $\mathcal{O}(1)$ — Fixed auxiliary space of size 10 to store digit counts.

---

## Code Implementations

### Python 3

```python
from collections import Counter

def findEvenNumbers(digits: list[int]) -> int:
    digit_counts = Counter(digits)
    distinct_even_count = 0

    # Iterate through all 3-digit even numbers
    for num in range(100, 1000, 2):
        d1 = num // 100         # Hundreds digit
        d2 = (num // 10) % 10   # Tens digit
        d3 = num % 10           # Units digit
        
        needed = Counter([d1, d2, d3])
        
        # Check if digit_counts has enough copies of each required digit
        if all(digit_counts[d] >= count for d, count in needed.items()):
            distinct_even_count += 1

    return distinct_even_count

# Driver Code
if __name__ == "__main__":
    print(findEvenNumbers([1, 2, 3, 4]))  # Output: 12
    print(findEvenNumbers([0, 2, 2]))     # Output: 2
    print(findEvenNumbers([6, 6, 6]))     # Output: 1
    print(findEvenNumbers([1, 3, 5]))     # Output: 0
```

---

### C++

```cpp
#include <iostream>
#include <vector>

int findEvenNumbers(const std::vector<int>& digits) {
    std::vector<int> count(10, 0);
    for (int d : digits) {
        count[d]++;
    }

    int distinct_even_count = 0;

    for (int num = 100; num < 1000; num += 2) {
        int d1 = num / 100;
        int d2 = (num / 10) % 10;
        int d3 = num % 10;

        std::vector<int> req(10, 0);
        req[d1]++;
        req[d2]++;
        req[d3]++;

        bool possible = true;
        for (int i = 0; i < 10; ++i) {
            if (req[i] > count[i]) {
                possible = false;
                break;
            }
        }

        if (possible) {
            distinct_even_count++;
        }
    }

    return distinct_even_count;
}

int main() {
    std::cout << findEvenNumbers({1, 2, 3, 4}) << std::endl; // Output: 12
    std::cout << findEvenNumbers({0, 2, 2}) << std::endl;    // Output: 2
    std::cout << findEvenNumbers({6, 6, 6}) << std::endl;    // Output: 1
    std::cout << findEvenNumbers({1, 3, 5}) << std::endl;    // Output: 0
    return 0;
}
```

---

### Java

```java
public class DistinctEvenNumbers {

    public static int findEvenNumbers(int[] digits) {
        int[] count = new int[10];
        for (int d : digits) {
            count[d]++;
        }

        int distinctEvenCount = 0;

        for (int num = 100; num < 1000; num += 2) {
            int d1 = num / 100;
            int d2 = (num / 10) % 10;
            int d3 = num % 10;

            int[] req = new int[10];
            req[d1]++;
            req[d2]++;
            req[d3]++;

            boolean possible = true;
            for (int i = 0; i < 10; i++) {
                if (req[i] > count[i]) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                distinctEvenCount++;
            }
        }

        return distinctEvenCount;
    }

    public static void main(String[] args) {
        System.out.println(findEvenNumbers(new int[]{1, 2, 3, 4})); // Output: 12
        System.out.println(findEvenNumbers(new int[]{0, 2, 2}));    // Output: 2
        System.out.println(findEvenNumbers(new int[]{6, 6, 6}));    // Output: 1
        System.out.println(findEvenNumbers(new int[]{1, 3, 5}));    // Output: 0
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).