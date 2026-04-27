from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [i for i in s if i in "aeiou"]
        a = Counter(vowels)
        vowels.sort(key=lambda c: (-a[c], s.index(c)))
        result = []
        vowel_idx = 0
        for j in s:
            if j in "aeiou":
                result.append(vowels[vowel_idx])
                vowel_idx += 1
            else:
                result.append(j)
        return "".join(result)
