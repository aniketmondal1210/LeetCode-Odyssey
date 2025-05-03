# Problem: Final Value of Variable After Performing Operations

You are given an array of strings `operations` representing operations that increment or decrement a variable `X` by 1.

The operations can be one of the following:
- `"++X"` or `"X++"`: Increment `X` by 1.
- `"--X"` or `"X--"`: Decrement `X` by 1.

Initially, `X` is set to 0. Return the final value of `X` after performing all operations in the array.

## Input
- `operations`: A list of strings representing the operations.

## Output
- An integer representing the final value of `X`.

## Example 1
```
Input: operations = ["--X", "X++", "X++"]
Output: 1
Explanation:
X = 0 -> -1 ("--X") -> 0 ("X++") -> 1 ("X++")
```

## Example 2
```
Input: operations = ["++X", "++X", "X++"]
Output: 3
Explanation:
X = 0 -> 1 -> 2 -> 3
```

## Example 3
```
Input: operations = ["X++", "++X", "--X", "X--"]
Output: 0
Explanation:
X = 0 -> 1 -> 2 -> 1 -> 0
```

## Constraints
- `1 <= operations.length <= 100`
- Each element in `operations` is one of `"++X"`, `"X++"`, `"--X"`, or `"X--"`
