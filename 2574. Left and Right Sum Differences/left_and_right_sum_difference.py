class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        summ = sum(nums)
        left_sum = 0
        result = []
        for i in nums:
            right_sum = summ - left_sum - i
            result.append(abs(left_sum - right_sum))
            left_sum += i
        return result
