class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []
        result = [words[0]]
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(result[-1]):
                result.append(words[i])
        return result
