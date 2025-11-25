class Solution:
    def splitArray(self, nums: List[int]) -> int:
        A = []
        B = []
        for j in range(len(nums)):
            if isPrime(j):
                A.append(nums[j])
            else:
                B.append(nums[j])
        return abs(sum(A) - sum(B))

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
