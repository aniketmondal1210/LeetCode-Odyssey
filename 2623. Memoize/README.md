# Problem: Memoize a Function

## Problem Statement
Given a function `fn`, return a **memoized** version of that function.

A **memoized function** stores the result of previous function calls, so if the same inputs are given again, it returns the cached value instead of recalculating it.

You can assume there are **three possible input functions**:  
- `sum`  
- `fib`  
- `factorial`

---

## Function Descriptions
- **sum(a, b)** → returns `a + b`  
  - Caching is based on ordered pairs.  
    - i.e., `(2, 3)` and `(3, 2)` are considered **different**.

- **fib(n)** → returns `1` if `n <= 1`, otherwise `fib(n - 1) + fib(n - 2)`.

- **factorial(n)** → returns `1` if `n <= 1`, otherwise `n * factorial(n - 1)`.

---

## Example 1
**Input:**

fnName = "sum"

actions = ["call","call","getCallCount","call","getCallCount"]

values = [[2,2],[2,2],[],[1,2],[]]


**Output:**

[4,4,1,3,2]


**Explanation:**
const sum = (a, b) => a + b;

const memoizedSum = memoize(sum);

memoizedSum(2, 2); // call → returns 4 (new call)

memoizedSum(2, 2); // call → returns 4 (cached)

getCallCount();    // → 1

memoizedSum(1, 2); // call → returns 3 (new call)

getCallCount();    // → 2

Example 2

Input:

fnName = "factorial"

actions = ["call","call","call","getCallCount","call","getCallCount"]

values = [[2],[3],[2],[],[3],[]]

Output:

[2,6,2,2,6,2]

Explanation:

const factorial = (n) => (n <= 1) ? 1 : n * factorial(n - 1);

const memoFactorial = memoize(factorial);


memoFactorial(2); // call → 2

memoFactorial(3); // call → 6

memoFactorial(2); // call → 2 (cached)

getCallCount();   // → 2

memoFactorial(3); // call → 6 (cached)

getCallCount();   // → 2

Example 3

Input:

fnName = "fib"

actions = ["call","getCallCount"]

values = [[5],[]]

Output:

[8,1]

Explanation:

fib(5) = 8

// Only one new call was made.

Constraints

0 ≤ a, b ≤ 10⁵

1 ≤ n ≤ 10

1 ≤ actions.length ≤ 10⁵

actions.length === values.length

actions[i] ∈ {"call", "getCallCount"}

fnName ∈ {"sum", "factorial", "fib"}
