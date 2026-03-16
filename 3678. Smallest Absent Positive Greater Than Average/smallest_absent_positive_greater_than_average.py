import math
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        newSet = set(nums)
        avg = sum(nums)/len(nums)
        start = max(1,math.floor(avg) + 1)
        while start in newSet:
            start += 1
        return start
