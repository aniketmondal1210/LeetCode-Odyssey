class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        count = 0
        for i in s:
            if i not in seen:
                seen.add(i)
                count += 1
        return count
