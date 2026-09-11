class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in range(len(nums)):
            digit = nums[i] + temp
            temp = digit
            result.append(digit)
        return result
