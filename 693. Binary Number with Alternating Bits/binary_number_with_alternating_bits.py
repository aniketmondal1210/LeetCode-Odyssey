class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)[2:]
        return False if "00" in a or "11" in a else True
