class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a = max(nums)
        count = 0
        for i in nums:
            if i != a:
                count += (a - i)
        return count
