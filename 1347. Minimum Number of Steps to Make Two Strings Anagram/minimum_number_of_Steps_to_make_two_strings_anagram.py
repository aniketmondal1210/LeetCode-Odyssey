class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if Counter(s) == Counter(t):
            return 0
        else:
            count = 0
            a = Counter(s)
            b = Counter(t)
            for key,values in b.items():
                if b[key] > a[key]:
                    count += (b[key] - a[key])
            return count
