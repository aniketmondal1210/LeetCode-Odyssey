class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = []
        while(n > 0):
            digits.append(n % 10)
            n //= 10
        summ = sum(digits)
        sq_summ = sum(i**2 for i in digits)
        return sq_summ - summ >= 50
