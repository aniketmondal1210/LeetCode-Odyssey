class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def max_digits(n):
            digits = sorted(str(abs(n)), reverse=True)
            val = int(''.join(digits))
            return -val if n < 0 else val
        gains = [max_digits(num) - num for num in nums]
        gains.sort(reverse=True)
        total = sum(nums)
        for i in range(min(k, len(gains))):
            if gains[i] > 0:
                total += gains[i]
            else:
                break
        return total
