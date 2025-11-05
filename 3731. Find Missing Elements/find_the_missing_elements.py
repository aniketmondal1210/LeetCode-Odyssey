class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        mini_val = min(nums)
        maxi_val = max(nums)
        missing = []
        for i in range(mini_val, maxi_val + 1):
            if i not in nums_set:
                missing.append(i)
        return sorted(missing)
