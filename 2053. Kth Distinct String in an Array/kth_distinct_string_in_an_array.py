from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = []
        a = Counter(arr)
        for key,value in a.items():
            if value == 1:
                result.append(key)
        return result[k-1] if len(result) >= k else ""
