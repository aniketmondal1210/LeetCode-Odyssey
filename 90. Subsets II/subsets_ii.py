from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        seen = set()
        for i in range(len(nums)+1):
            for subsets in combinations(nums, i):
                if subsets not in seen:
                    seen.add(subsets)
                    result.append(subsets)
        return [list(j) for j in result]
