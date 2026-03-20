from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        a = [i for i in nums if i % 2 == 0]
        if not a:
            return -1
        b = Counter(a)
        c = max(b.values())
        result = []
        for key, value in b.items():
            if value == c:
                result.append(key)
        return min(result)
