class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            a = bin(n)[2:]
            if a.count('1') == 1:
                return True
            else:
                return False
