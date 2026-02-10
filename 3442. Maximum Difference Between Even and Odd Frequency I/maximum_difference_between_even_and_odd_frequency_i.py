from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        a = Counter(s)
        maxi = float('-inf')
        mini = float('inf')
        for key,value in a.items():
            if value % 2 == 0:
                mini = min(mini,value)
            else:
                maxi = max(maxi,value)
        return maxi - mini
