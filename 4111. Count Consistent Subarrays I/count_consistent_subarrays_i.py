class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            current_min = nums[i]
            current_and = nums[i]
            for j in range(i, len(nums)):
                current_min = min(current_min, nums[j])
                current_and &= nums[j]
                if current_min == current_and:
                    count += 1
        return count
