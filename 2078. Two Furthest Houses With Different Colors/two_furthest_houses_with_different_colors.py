class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        i, j = 0, n - 1
        while colors[i] == colors[j]:
            j -= 1
        a = j - i
        
        i, j = 0, n - 1
        while colors[i] == colors[j]:
            i += 1
        b = j - i
        return max(a, b)
