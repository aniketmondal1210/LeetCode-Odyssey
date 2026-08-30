class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        summ = 0
        for i in nums:
            width = i % 10
            d = i // 10
            s = str(d)
            xi = int(s[:width])
            yi = int(s[width:])
            decoded = pow(xi,yi,MOD)
            summ += decoded
        return summ % MOD
