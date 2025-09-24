class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)

        result = ""
        while(num != 0):
            rem = (num % 7)
            result += str(rem)
            num //= 7

        result = result[::-1]
        return "-" + result if negative else result
