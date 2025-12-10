class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for i in words:
            parts = i.split(separator)
            for j in parts:
                if j:
                    result.append(j)
        return result
