class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i in s:
            a = s.index(i)
            b = t.index(i)
            result += abs(a - b)
        return result
