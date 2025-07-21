class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        result = []
        new_nums = nums
        while(len(new_nums) > 0):
            max_val = max(nums)
            min_val = min(nums)
            avg = (max_val + min_val)/2
            result.append(avg)
            new_nums.remove(max_val)
            new_nums.remove(min_val)
        return len(set(result))
