class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ''
        for i in range(len(s)):
            a += str(ord(s[i]) - ord('a') + 1)
        for j in range(k):
            summ = 0
            for l in a:
                summ += int(l)
            a = str(summ)
        return summ
