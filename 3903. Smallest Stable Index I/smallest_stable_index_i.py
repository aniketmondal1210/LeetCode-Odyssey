class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            maxi = max(nums[:i + 1])
            mini = min(nums[i:])
            instability = maxi - mini
            if instability <= k:
                return i
        return -1
