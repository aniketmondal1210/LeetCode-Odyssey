from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        a = Counter(word)
        sorted_word = sorted(a.values(), reverse=True)
        summ = 0
        for i in range(len(sorted_word)):
            if 0 <= i <= 7:
                summ += sorted_word[i] * 1
            elif 8 <= i <= 15:
                summ += sorted_word[i] * 2
            elif 16 <= i <= 23:
                summ += sorted_word[i] * 3
            else:
                summ += sorted_word[i] * 4
        return summ
