class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s) - 1):
            a = int(s[i])
            b = int(s[i + 1])
            if abs(a - b) > 2:
                return False
        return True
