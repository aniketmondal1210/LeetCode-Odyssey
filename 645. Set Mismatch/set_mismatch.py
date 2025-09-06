from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        for key in nums:
            if a[key] == 2:
                repeated_num = key
        n = len(nums)
        nums_set = list(set(nums))
        missing_num = (n*(n+1))//2 - sum(nums_set)
        return [repeated_num,missing_num]
