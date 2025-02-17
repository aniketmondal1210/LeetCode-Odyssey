class Solution:
    def scoreOfString(self, s: str) -> int:
        a = 0
        for i in range(len(s)-1):
            b = abs(ord(s[i])-ord(s[i+1]))
            a+=b
        return a
