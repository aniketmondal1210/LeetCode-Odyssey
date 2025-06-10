class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ""
        a = 10**9 + 7
        for i in range(1,n+1):
            result += str(bin(i)[2:])
        return int(result,2) % a
