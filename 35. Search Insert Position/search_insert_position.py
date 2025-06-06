class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
            else:
                start = 0
                end = len(nums) - 1
                while(start <= end):
                    mid = (start + end)//2
                    if nums[mid] == target:
                        return mid
                    elif target < nums[mid]:
                        end = mid - 1
                    elif target > nums[mid]:
                        start = mid + 1
                return start
