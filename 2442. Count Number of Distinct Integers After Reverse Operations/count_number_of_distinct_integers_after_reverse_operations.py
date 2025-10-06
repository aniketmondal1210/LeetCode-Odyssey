class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_nums = list(set(nums))
        for i in new_nums:
            nums.append(int(str(i)[::-1]))
        return len(set(nums))
