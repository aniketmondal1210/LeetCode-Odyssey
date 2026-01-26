class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = []
        for i in range(len(nums) - k + 1):
            a = nums[i:i+k]
            b = abs(max(a)-min(a))
            result.append(b)
        return min(result)
