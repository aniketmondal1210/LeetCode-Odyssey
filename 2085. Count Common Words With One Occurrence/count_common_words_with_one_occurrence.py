from collections import Counter
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = Counter(words1)
        b = Counter(words2)
        count = 0
        for word in a:
            if word in b and a[word] == 1 and b[word] == 1:
                count += 1
        return count
