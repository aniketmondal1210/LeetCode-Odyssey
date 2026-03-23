import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            curr = nums[i]
            if curr == k:
                count += 1
            for j in range(i + 1, n):
                curr = (curr * nums[j]) // math.gcd(curr, nums[j])
                if curr == k:
                    count += 1
                elif curr > k:
                    break
        return count
