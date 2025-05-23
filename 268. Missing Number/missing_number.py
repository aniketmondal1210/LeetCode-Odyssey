class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        for i in range(a):
            if i not in nums:
                return i
                break
        return a+1
