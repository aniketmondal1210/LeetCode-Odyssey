class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        summ = 0
        while left <= right:
            if left == right:
                summ += nums[left]
            else:
                summ += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        return summ
