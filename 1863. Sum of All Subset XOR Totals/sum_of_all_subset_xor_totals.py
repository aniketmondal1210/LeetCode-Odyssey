from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)+1):
            for subset in combinations(nums,i):
                subset_xor = 0
                for num in subset:
                    subset_xor ^= num
                result.append(subset_xor)
        return sum(result)
