import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = math.prod([i for i in nums if i != 0])
        zero_count = nums.count(0)
        for i in range(len(nums)):
            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1:
                nums[i] = a if nums[i] == 0 else 0
            else:
                nums[i] = a // nums[i]
        return nums
