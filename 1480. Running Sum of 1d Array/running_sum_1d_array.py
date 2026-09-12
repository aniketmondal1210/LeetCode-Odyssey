class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in range(len(nums)):
            summ = nums[i] + temp
            temp = summ
            result.append(summ)
        return result
