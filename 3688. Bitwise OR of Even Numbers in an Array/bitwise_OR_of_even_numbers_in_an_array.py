class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if i % 2 == 0:
                result |= i
        return result
