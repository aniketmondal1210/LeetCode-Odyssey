from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        result = []
        for key,value in a.items():
            if value == 2:
                result.append(key)
        return result
