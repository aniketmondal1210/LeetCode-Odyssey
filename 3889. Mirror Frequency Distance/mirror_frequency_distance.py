from collections import Counter
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        a = Counter(s)
        total = 0
        seen = set()
        for i in a:
            if i in seen:
                continue
            if i.isalpha():
                m = chr(122 - ord(i) + 97)
            else:
                m = str(9 - int(i))
            total += abs(a[i] - a.get(m, 0))
            seen.add(i)
            seen.add(m)
        return total
