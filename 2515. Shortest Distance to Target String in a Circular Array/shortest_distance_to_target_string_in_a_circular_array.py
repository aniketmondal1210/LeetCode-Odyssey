class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1
        
        mini = float('inf')
        for i in range(n):
            if words[i] == target:
                right = (i - startIndex + n) % n
                left = n - right
                mini = min(mini, right, left)
        return mini
