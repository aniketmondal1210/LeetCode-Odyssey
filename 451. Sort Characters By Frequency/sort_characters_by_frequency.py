from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        a = Counter(s)
        b = sorted(a.items(), key=lambda x: x[1], reverse=True)
        for char, freq in b:
            result += char * freq
        return result
