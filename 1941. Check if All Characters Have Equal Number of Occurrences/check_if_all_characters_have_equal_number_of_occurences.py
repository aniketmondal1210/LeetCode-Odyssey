from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        return len(set(a.values())) == 1
