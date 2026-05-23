class Solution:
    def check(self, nums: List[int]) -> bool:
        a = nums[:]
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i:] + nums[:i] == a:
                return True
        return False
