class Solution:
    def minRotations(self, s: str) -> int:
        def rotations(a, b):
            return min(abs(a - b), 10 - abs(a - b))
        
        summ = rotations(0, int(s[0]))
        for i in range(1, len(s)):
            summ += rotations(int(s[i-1]), int(s[i]))
        return summ
