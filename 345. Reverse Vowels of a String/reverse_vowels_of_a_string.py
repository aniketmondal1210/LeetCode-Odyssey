class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowel_s = []
        for i in s:
            if i in vowels:
                vowel_s.append(i)
        new_s = ''
        for j in range(len(s)):
            if s[j] in vowels:
                new_s += vowel_s.pop()
            else:
                new_s += s[j]
        return new_s
