class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        result = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                result.append(nums[i])
            else:
                break
        a = sum(result)
        while a in nums:
            a += 1
        return a
