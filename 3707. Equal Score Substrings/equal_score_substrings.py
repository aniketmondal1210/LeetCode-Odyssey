class Solution:
    def scoreBalance(self, s: str) -> bool:
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            left_sum = sum(ord(ch) - ord('a') + 1 for ch in left)
            right_sum = sum(ord(ch) - ord('a') + 1 for ch in right)
            
            if left_sum == right_sum:
                return True
        return False
