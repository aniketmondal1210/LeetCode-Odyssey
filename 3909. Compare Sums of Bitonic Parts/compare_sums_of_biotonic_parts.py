class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asc_sum = 0
        desc_sum = 0
        max_idx = 0
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_idx = i
            else:
                break
                
        for i in range(max_idx + 1):
            asc_sum += nums[i]
        for j in range(max_idx, len(nums)):
            desc_sum += nums[j]
    
        if asc_sum > desc_sum:
            return 0
        elif asc_sum < desc_sum:
            return 1
        else:
            return -1
