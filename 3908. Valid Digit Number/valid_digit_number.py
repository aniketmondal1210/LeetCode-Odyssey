class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        a = str(n)
        return str(x) in a and a[0] != str(x)
