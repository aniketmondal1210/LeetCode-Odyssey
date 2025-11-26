class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original_num = n
        summ = 0
        prod = 1
        while(n > 0):
            digit = n % 10
            n //= 10
            summ += digit
            prod *= digit
        return original_num % (summ + prod) == 0
