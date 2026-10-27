class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        if not nums or len(nums) == 1:
            return nums[0] if nums else 0
        arr = nums.copy()
        while len(arr) > 1:
            result = []
            for i in range(len(arr) - 1):
                result.append((arr[i] + arr[i + 1]) % 10)
            arr = result
        return arr[0]
