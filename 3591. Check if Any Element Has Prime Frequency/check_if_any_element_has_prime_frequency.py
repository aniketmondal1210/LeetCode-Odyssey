from collections import Counter
import math
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        a = Counter(nums)
        for key,value in a.items():
            if value > 1 and is_prime(value):
                return True
        return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
