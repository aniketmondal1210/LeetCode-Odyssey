class Solution:
    def maxProductPair(self, nums: List[int], target: int) -> List[int]:
        max_prod = float('-inf')
        pair = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target) and (nums[i] > nums[j]):
                    product = nums[i] * nums[j]
                    if product > max_prod:
                        max_prod = product
                        pair = [i, j]
        return pair
