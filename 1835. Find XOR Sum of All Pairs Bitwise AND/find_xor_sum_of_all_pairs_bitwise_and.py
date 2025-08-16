class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor_arr1 = 0
        xor_arr2 = 0
        for i in arr1:
            xor_arr1 ^= i
        for j in arr2:
            xor_arr2 ^= j
        return xor_arr1 & xor_arr2
