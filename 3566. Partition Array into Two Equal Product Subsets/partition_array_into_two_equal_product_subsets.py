import math
from itertools import combinations
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        nums_set = set(nums)

        for i in range(1,n):
            for subset in combinations(nums,i):
                if math.prod(subset) == target:
                    rem = nums_set - set(subset)
                    if rem and math.prod(rem) == target:
                        return True
        return False
