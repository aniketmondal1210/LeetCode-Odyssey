class Solution:
    def sumBase(self, n: int, k: int) -> int:
        summ = 0
        result = []

        if n == 0:
            return 0
        
        while(n > 0):
            rem = n % k
            result.append(rem)
            n //= k
        
        for i in result:
            summ += i

        return summ
