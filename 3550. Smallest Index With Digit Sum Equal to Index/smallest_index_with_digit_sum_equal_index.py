class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == sum_of_digit(nums[i]):
                return i
        return -1

        
def sum_of_digit(n):
    return sum((int(digit)) for digit in str(n))
