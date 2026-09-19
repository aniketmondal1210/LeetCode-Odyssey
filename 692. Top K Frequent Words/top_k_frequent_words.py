from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        a = Counter(words)
        sorted_words = sorted(a, key=lambda x: (-a[x], x))
        return sorted_words[:k]
