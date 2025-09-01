from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        a = Counter(nums)
        result = 0
        for key,value in a.items():
            if value == 2:
                result ^= key
        return result
