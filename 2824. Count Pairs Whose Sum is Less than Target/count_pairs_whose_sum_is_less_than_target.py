class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < target:
                    result.append([i,j])
        return len(result)
