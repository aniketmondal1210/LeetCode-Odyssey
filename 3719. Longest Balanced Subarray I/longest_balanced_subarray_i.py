class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            even_set = set()
            odd_set = set()
            for j in range(i,len(nums)):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(even_set) == len(odd_set):
                    max_len = max(j-i+1,max_len)
        return max_len
