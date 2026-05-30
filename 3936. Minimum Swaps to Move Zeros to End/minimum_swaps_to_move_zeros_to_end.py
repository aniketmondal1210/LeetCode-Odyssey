class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        a = nums.count(0)
        count = 0
        for i in range(len(nums) - a):
            if nums[i] == 0:
                count += 1
        return count
