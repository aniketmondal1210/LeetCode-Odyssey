class Solution:
    def sortSentence(self, s: str) -> str:
        result = ""
        b = []
        a = s.split()
        for i in a:
            pos = int(i[-1])
            word = i[:-1]
            b.append((pos, word))
        b.sort()
        for j in b:
            result += (j[1] + " ")
        return result[:-1]
