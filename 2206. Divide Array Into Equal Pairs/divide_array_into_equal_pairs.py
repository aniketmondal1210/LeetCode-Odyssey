from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
            
        a = Counter(nums)
        for key, value in a.items():
            if value % 2 != 0:
                return False
        return True
