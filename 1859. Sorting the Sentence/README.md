# Reconstruct Original Sentence from Shuffled Version

## Problem Statement

A sentence is a list of words separated by a single space, with no leading or trailing spaces. Each word contains only lowercase and uppercase English letters.

A shuffled sentence is formed by appending the 1-indexed position to each word, and then rearranging the words arbitrarily.

Given a shuffled sentence `s` (with no more than 9 words), reconstruct and return the **original sentence**.

## Examples

### Example 1:

Input:  
`s = "is2 sentence4 This1 a3"`  
Output:  
`"This is a sentence"`  
Explanation:  
Sorted by the trailing digit: `"This1 is2 a3 sentence4"`  
Removing numbers: `"This is a sentence"`

### Example 2:

Input:  
`s = "Myself2 Me1 I4 and3"`  
Output:  
`"Me Myself and I"`  
Explanation:  
Sorted: `"Me1 Myself2 and3 I4"`  
Removing numbers: `"Me Myself and I"`

## Constraints

- `2 <= s.length <= 200`
- `s` consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
- The number of words in `s` is between 1 and 9.
- Words are separated by a single space.
- No leading or trailing spaces in `s`.
