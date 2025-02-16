class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        a = 0
        while(x>0):
            b = x % 10
            a += b
            x //= 10
        if(temp % a == 0):
            return a
        else:
            return -1
