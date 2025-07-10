class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(1,len(s)+1):
            reverse_value = 123 - ord(s[i-1])
            result += reverse_value*i
        return result
