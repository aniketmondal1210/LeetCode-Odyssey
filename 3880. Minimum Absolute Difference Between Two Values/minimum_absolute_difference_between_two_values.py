class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        arr_1 = []
        arr_2 = []
        for i in range(len(nums)):
            if nums[i] == 1:
                arr_1.append(i)
            elif nums[i] == 2:
                arr_2.append(i)
        if not arr_1 or not arr_2:
            return -1
        mini = float('inf')
        for k in arr_1:
            for l in arr_2:
                mini = min(mini, abs(k - l))
        return mini
