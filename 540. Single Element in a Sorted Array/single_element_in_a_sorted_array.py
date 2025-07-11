from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for key,value in a.items():
            if value < 2:
                return key
        return -1
