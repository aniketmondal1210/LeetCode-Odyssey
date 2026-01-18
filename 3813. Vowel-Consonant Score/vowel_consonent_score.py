class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set('aeiou')
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i.lower() in vowels:
                    v += 1
                else:
                    c += 1
        if c > 0:
            return v // c
        else:
            return 0
