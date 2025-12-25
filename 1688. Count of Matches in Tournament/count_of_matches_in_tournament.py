class Solution:
    def numberOfMatches(self, n: int) -> int:
        summ = 0
        while(n > 1):
            if n % 2 == 0:
                summ += (n // 2)
                n = (n // 2)
            else:
                summ += ((n-1) // 2)
                n = ((n - 1) // 2) + 1
        return summ
