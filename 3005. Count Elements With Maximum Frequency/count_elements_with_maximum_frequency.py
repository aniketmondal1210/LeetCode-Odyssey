from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = Counter(nums)
        count = 0
        max_val = max(a.values())
        for key,value in a.items():
            if value == max_val:
                count += 1
        return count * max_val
