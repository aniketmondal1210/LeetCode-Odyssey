class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        flag = False
        for i in range(2,n-2):
            a = convert_to_base(n,i)
            if a[::-1] == a:
                flag = True
            flag = False
        return flag

def convert_to_base(x, base):
    digits = ""
    while(x > 0):
        digits += str(x % base)
        x //= base
    return digits[::-1]
