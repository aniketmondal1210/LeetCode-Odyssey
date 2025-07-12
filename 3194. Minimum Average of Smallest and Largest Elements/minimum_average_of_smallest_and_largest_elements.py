class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        result = []
        while(nums != []):
            a = (max(nums)+min(nums))/2
            result.append(a)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(result)
