class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        result = []
        for i in range(len(nums)):
            if nums[i] == 1:
                result.append(i)
        for j in range(len(result)-1):
            if abs(result[j] - result[j+1]) <= k:
                return False
        return True
