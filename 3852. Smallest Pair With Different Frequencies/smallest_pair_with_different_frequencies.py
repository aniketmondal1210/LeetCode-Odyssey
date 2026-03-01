from collections import Counter
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        a = Counter(nums)
        x = min(nums)
        b = a[x]
        for key in sorted(a.keys()):
            if key > x and a[key] != b:
                return [x, key]
        return [-1, -1]
