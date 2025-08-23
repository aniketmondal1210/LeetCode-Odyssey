class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        result = []
        for i in range(1,a+1):
            if b % i == 0 and a % i == 0:
                result.append(i)
        return max(result)
