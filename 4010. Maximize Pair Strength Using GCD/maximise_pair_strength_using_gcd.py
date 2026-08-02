import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                hcf = math.gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (hcf * hcf)
                if strength > maxi:
                    maxi = strength
        return maxi
