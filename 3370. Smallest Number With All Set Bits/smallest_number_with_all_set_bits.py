class Solution:
    def smallestNumber(self, n: int) -> int:
        a = bin(n)[2:]
        return int(a.replace('0','1'),2)
