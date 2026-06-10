class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        summ = 0
        start = max(1, n - k)
        end = n + k
        for i in range(start,end+1):
            if abs(n-i) <= k and (n & i) == 0:
                summ += i
        return summ
