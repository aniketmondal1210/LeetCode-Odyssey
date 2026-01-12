import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i < j and math.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1])) == 1:
                    count += 1
        return count
