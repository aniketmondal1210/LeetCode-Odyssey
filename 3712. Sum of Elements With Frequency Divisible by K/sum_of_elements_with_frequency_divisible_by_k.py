from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        a = Counter(nums)
        result = 0
        for key, value in a.items():
            if value % k == 0:
                result += (key * value)
        return result
