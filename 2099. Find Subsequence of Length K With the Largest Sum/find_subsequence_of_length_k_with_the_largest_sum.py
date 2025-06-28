class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new_nums = nums
        for i in range(len(nums)-k):
            new_nums.remove(min(new_nums))
        return new_nums
