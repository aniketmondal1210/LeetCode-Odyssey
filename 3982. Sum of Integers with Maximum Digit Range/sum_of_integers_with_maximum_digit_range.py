class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_dr = 0
        for i in nums:
            dr = digit_range(i)
            if dr > max_dr:
                max_dr = dr
        summ = 0
        for j in nums:
            if max_dr == digit_range(j):
                summ += j
        return summ

def digit_range(n):
    digits = [int(d) for d in str(n)]
    return max(digits) - min(digits)
