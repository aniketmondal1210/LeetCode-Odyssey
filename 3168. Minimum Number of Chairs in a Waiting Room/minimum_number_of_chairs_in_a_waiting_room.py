class Solution:
    def minimumChairs(self, s: str) -> int:
        curr = 0
        maxi = 0
        for i in s:
            if i == 'E':
                curr += 1
                maxi = max(maxi, curr)
            else:
                curr -= 1
        return maxi
