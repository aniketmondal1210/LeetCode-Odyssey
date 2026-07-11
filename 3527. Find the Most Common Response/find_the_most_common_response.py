from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        result = []
        for i in responses:
            result.append(set(i))
        new_result = []
        for j in result:
            for k in j:
                new_result.append(k)
        a = Counter(new_result)
        sorted_new_result = sorted(new_result, key=lambda x: (-a[x], x))
        return sorted_new_result[0]
