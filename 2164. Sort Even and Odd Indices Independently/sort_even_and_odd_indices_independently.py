class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[0:len(nums):2])
        odd = sorted(nums[1:len(nums):2], reverse=True)
        i, j = 0, 0
        result = []
        for k in range(len(nums)):
            if k % 2 == 0:
                result.append(even[i])
                i += 1
            else:
                result.append(odd[j])
                j += 1
        return result
