class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        a = set(word.lower())
        for lower in a:
            upper = lower.upper()
            if lower in word and upper in word and word.rfind(lower) < word.find(upper):
                count += 1
        return count
