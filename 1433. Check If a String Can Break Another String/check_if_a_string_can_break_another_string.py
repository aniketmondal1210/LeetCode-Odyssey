class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        n = len(sorted_s1)
        s1_breaks_s2 = all(sorted_s1[i] >= sorted_s2[i] for i in range(n))
        s2_breaks_s1 = all(sorted_s2[i] >= sorted_s1[i] for i in range(n))
        return s1_breaks_s2 or s2_breaks_s1
