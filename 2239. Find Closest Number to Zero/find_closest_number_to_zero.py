class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = float('inf')
        num = 0
        for i in nums:
            if abs(i) < dist:
                dist = abs(i)
                num = i
            elif abs(i) == dist and i > num:
                num = i
        return num
