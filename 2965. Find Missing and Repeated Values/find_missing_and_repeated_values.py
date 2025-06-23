from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = []
        for i in grid:
            for j in i:
                result.append(j)
        a = Counter(result)
        n = len(result)
        for key, value in a.items():
            if value > 1:
                repeating_num = key
        missing_num = (n * (n + 1)) // 2 - sum(list(set(result)))
        return [repeating_num, missing_num]
