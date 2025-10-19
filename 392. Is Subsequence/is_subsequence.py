class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = iter(t)
        return all(ch in a for ch in s)
