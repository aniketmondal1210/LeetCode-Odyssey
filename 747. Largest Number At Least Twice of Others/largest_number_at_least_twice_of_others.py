class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        new_nums = list(set(nums))
        new_nums.sort(reverse = True)
        a = new_nums[0]
        b = new_nums[1]
        return nums.index(a) if a >= 2*b else -1
