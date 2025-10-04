class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+11):
            if product_of_digits(i) % t == 0:
                return i


def product_of_digits(num):
    mul = 1
    while(num>0):
        digit = num % 10
        mul *= digit
        num //= 10
    return mul
