from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        a = Counter(nums)
        for i in nums:
            if i % 2 == 0 and a[i] == 1:
                return i
        return -1
