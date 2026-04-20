class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_lower = word.lower()
        word_set = set(word_lower)
        count = 0
        for i in word_set:
            if i in word and i.upper() in word:
                count += 1
        return count
