from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a = Counter(str(n))
        summ = 0
        for key, value in a.items():
            summ += int(key) * value
        return summ
