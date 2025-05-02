class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_arr = []
        temp = 0
        for i in range(len(nums)):
            digit = nums[i] + temp
            temp = digit
            new_arr.append(digit)
        return new_arr
