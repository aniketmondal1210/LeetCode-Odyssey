class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            substr = s[i:i+2]
            if substr in s[::-1]:
                return True
        return False
