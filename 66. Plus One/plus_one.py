class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_str = ""
        for i in digits:
            digit_str += str(i)
        sum_digit = int(digit_str) + 1
        return [int(j) for j in str(sum_digit)]
