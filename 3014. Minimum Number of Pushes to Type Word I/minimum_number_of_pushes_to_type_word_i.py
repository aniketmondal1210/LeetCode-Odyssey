class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        summ = 0
        for i in range(n):
            if 0 <= i <= 7:
                summ += 1
            elif 8 <= i <= 15:
                summ += 2
            elif  16 <= i <= 23:
                summ += 3
            else:
                summ += 4
        return summ 
