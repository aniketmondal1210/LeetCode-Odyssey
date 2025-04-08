class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in sentences:
            words = i.split()
            num_words = len(words)
            if num_words > max:
                max = num_words
        return max
