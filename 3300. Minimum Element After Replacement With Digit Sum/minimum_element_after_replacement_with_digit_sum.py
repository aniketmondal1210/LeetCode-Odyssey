class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = 99999
        for i in nums:
            a = digit_sum(i)
            if a < mini:
                mini = a
        return mini

def digit_sum(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result
