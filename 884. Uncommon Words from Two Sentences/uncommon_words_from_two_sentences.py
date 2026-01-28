class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        common = set(s1).intersection(set(s2))
        result = []
        for i in s1:
            if i not in common and s1.count(i) == 1:
                result.append(i)
        for j in s2:
            if j not in common and s2.count(j) == 1:
                result.append(j)
        return result
