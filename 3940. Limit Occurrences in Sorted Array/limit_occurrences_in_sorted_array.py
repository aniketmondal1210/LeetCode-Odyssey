from collections import Counter
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        a = Counter(nums)
        result = []
        for i in a:
            result.extend([i]*min(k,a[i]))
        return result
