class Solution:
    def possibleStringCount(self, word: str) -> int:
        if len(set(word)) == len(word):
            return 1
        elif len(set(word)) == 1:
            return len(word)
        else:
            summ = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    summ += 1    
            return summ
