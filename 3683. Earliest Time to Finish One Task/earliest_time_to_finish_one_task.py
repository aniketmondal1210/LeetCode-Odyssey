class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float('inf')
        for i in tasks:
            s = i[0]
            t = i[1]
            ans = min(ans, s + t)
        return ans
