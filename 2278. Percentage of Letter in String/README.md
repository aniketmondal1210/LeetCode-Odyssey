# Problem: Percentage of Letter in String

Given a string `s` and a character `letter`, return the percentage of characters in `s` that are equal to `letter`, rounded down to the nearest whole percent.

## Input
- `s`: A string of lowercase English letters.
- `letter`: A single lowercase English letter.

## Output
- An integer representing the percentage (rounded down) of `letter` occurrences in `s`.

## Example 1
```
Input: s = "foobar", letter = "o"
Output: 33
Explanation: 2 out of 6 characters are 'o' → 2/6 * 100 = 33.33 → 33%
```

## Example 2
```
Input: s = "jjjj", letter = "k"
Output: 0
Explanation: 0 out of 4 characters are 'k' → 0/4 * 100 = 0%
```

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter.
