class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            new_arr.append(nums[nums[i]])
        return new_arr
