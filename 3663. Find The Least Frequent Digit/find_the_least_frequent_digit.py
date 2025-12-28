from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        a = Counter(str(n))
        b = min(a.values())
        c = [key for key,value in a.items() if value == b]
        return int(min(c))
