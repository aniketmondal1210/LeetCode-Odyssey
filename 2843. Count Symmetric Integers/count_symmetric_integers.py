class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 0:
                first_half = s[:n//2]
                second_half = s[n//2:]
                if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
                    count += 1
        return count
