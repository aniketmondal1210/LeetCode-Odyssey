class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for i in s:
            if len(result) >= 2 and result[-1] == i and result[-2] == i:
                continue
            result.append(i)
        return "".join(result)
