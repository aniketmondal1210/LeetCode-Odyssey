class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        b = max(nums)
        a = min(nums)
        for i in nums:
            if a < i < b:
                count += 1
        return count
