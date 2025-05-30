class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for i in nums:
            x+=i
        for j in nums:
            y += digit_sum(j)
        return abs(x-y)


def digit_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum        
