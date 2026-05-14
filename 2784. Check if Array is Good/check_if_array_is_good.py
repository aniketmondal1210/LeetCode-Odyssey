class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi = max(nums)
        if len(nums) != maxi + 1:
            return False
        a = Counter(nums)
        for i in range(1,maxi):
            if a[i] != 1:
                return False
        if a[maxi] != 2:
            return False
        return True
