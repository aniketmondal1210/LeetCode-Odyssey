class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_sum = 0
        for num in set(nums):
            if nums.count(num) == 1:
                unique_sum += num
        return unique_sum
