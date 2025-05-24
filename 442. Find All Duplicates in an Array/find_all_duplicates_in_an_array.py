from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        a = Counter(nums)
        for key, value in a.items():
            if value > 1:
                result.append(key)
        return result
