class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        for i in range(a):
            if i not in nums:
                return i
                break
        return a+1



OR



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_nums = 0
        xor_all = 0
        for i in nums:
            xor_nums ^= i
        for j in range(len(nums)+1):
            xor_all ^= j
        return xor_nums ^ xor_all
