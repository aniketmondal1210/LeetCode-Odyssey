class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        a = s.index('1')
        b = len(s) - 1 - s[::-1].index('1')
        return False if '0' in s[a:b+1] else True
