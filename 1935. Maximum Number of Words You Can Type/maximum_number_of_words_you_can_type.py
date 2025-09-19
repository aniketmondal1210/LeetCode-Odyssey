class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        count = 0
        for i in text.split():
            if not any(char in broken_set for char in i):
                count += 1
        return count
