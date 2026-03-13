class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        vowels_s = [i for i in s if i in vowels]
        vowels_s.sort()
        new_s = ""
        j = 0
        for i in range(len(s)):
            if s[i] not in vowels:
                new_s += s[i]
            else:
                new_s += vowels_s[j]
                j += 1
        return new_s
