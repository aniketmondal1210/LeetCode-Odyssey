from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] == nums[j] == nums[k] and (j - i) == (k - j):
                        count = nums.count(nums[i])
                        if count == 3:
                            seen.add(nums[i])
        return len(seen)
