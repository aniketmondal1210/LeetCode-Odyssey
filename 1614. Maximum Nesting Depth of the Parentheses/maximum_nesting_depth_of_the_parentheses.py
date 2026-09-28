class Solution:
    def maxDepth(self, s: str) -> int:
        left_parentheses = 0
        right_parentheses = 0
        ans = 0
        for i in s:
            if i == '(':
                left_parentheses += 1
            if i == ')':
                right_parentheses += 1
            ans = max(ans, left_parentheses - right_parentheses)
        return ans
