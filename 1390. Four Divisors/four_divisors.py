import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        summ = 0
        for j in nums:
            if len(divisors(j)) == 4:
                summ += sum(divisors(j))
        return summ


def divisors(n):
    small_divs = []
    large_divs = []
    
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            small_divs.append(i)
            if i != n // i:
                large_divs.append(n // i)
    
    return small_divs + large_divs[::-1]
