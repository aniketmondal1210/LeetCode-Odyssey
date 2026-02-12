from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        result = sorted(a,key=lambda x:a[x],reverse=True)
        return result[:k]
