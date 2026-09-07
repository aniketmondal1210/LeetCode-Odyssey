class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        result = []
        for i in sentence.split():
            for j in dictionary:
                if i.startswith(j):
                    result.append(j)
                    break
            else:
                result.append(i)
        return " ".join(result)
