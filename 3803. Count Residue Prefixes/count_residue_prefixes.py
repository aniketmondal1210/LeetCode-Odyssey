class Solution:
    def residuePrefixes(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            a = s[:i+1]
            a_set = len(set(a))
            a_modulo = len(a) % 3
            if a_set == a_modulo:
                count += 1
        return count
