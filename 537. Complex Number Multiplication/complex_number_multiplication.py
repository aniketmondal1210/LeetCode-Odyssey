class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1,b1 = func(num1)
        a2,b2 = func(num2)
        real = a1 * a2 - b1 * b2
        imag = a1 * b2 + a2 * b1
        return f"{real}+{imag}i"

def func(num):
    num = num[:-1]
    a, b = num.split('+')
    return int(a), int(b)
