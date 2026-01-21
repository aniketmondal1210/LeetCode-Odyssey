class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        for i in range(l, r + 1):
            for j in range(len(nums) - i + 1):
                subarray = nums[j:j + i]
                if sum(subarray) > 0:
                    mini = min(mini, sum(subarray))
        return mini if mini != float('inf') else -1
