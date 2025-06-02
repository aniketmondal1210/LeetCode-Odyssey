from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(n+1):
            for subset in combinations(nums,i):
                result.append(subset)
        return result
