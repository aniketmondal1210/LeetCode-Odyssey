class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lc = 0
        rc = 0
        l = len(s)
        for i in range(l//2):
            if s[i] in vowels:
                lc += 1
        for j in range(l//2,l):
            if s[j] in vowels:
                rc += 1
        return lc == rc
