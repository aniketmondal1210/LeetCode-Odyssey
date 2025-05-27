from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        Vowels = ['a','e','i','o','u']
        result = 0
        a = Counter(s)
        max_vowel_freq = 0
        max_consonant_freq = 0
        for key, value in a.items():
            if key in Vowels:
                max_vowel_freq = max(max_vowel_freq,value)
            else:
                max_consonant_freq = max(max_consonant_freq,value)
        return max_vowel_freq + max_consonant_freq
