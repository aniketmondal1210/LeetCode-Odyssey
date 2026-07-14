from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        sorted_nums = sorted(nums,key = lambda x: (a[x],-x))
        return sorted_nums
