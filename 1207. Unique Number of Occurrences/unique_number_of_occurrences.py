from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        result = []
        for key,value in a.items():
            result.append(value)
        return len(result) == len(set(result))
