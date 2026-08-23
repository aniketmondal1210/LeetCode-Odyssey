class Solution:
    def isPalindromic(self, s: str) -> bool:
        result = ""
        for i in s:
            result += format(ord(i), '08b')
        return result == result[::-1]
