class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        a = nums
        b = str(digit)
        count = 0
        for i in a:
            count += str(i).count(b)
        return count
