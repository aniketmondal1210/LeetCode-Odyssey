class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = s+t
        result = 0
        for i in a:
            result ^= ord(i)
        return chr(result)
