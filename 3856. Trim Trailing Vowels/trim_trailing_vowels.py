class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip('aeiou')


OR


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = "aeiou"
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in vowels:
                return s[:i + 1]
        return ""
