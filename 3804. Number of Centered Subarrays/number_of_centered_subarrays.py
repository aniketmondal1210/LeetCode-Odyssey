class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count = 0
        subarrays = get_all_subarrays(nums)
        for subarray in subarrays:
            if sum(subarray) in subarray:
                count += 1
        return count

def get_all_subarrays(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            result.append(nums[i:j+1])
    return result
