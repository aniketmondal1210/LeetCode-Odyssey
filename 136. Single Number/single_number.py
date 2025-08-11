from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = dict(Counter(nums))
        for key,value in a.items():
            if value == 1:
                return key



OR 



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
