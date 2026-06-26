class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for i in range(1, len(words)):
            current_word_letters = list(words[i])
            next_result = []
            for i in result:
                if i in current_word_letters:
                    next_result.append(i)
                    current_word_letters.remove(i)
            result = next_result
        return result
