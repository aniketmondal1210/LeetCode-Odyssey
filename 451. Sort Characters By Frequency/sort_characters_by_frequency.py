from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        a = Counter(s)
        sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=True)
        for char, freq in sorted_items:
            result += char * freq
        return result
