from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        a = Counter(nums)
        for key,value in a.items():
            if value == n:
                return key
