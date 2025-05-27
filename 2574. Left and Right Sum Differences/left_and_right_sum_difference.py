class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sums = [0]
        right_sums = [0]

        left_total = 0
        for num in nums:
            left_total += num
            left_sums.append(left_total)
        left_sums = left_sums[:-1]

        right_total = 0
        for num in reversed(nums):
            right_total += num
            right_sums.append(right_total)
        right_sums = right_sums[:-1]
        right_sums.reverse()

        result = [abs(left - right) for left, right in zip(left_sums, right_sums)]
        return result
