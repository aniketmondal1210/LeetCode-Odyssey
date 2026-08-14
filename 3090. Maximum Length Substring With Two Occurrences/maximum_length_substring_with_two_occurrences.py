from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxi = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                a = Counter(substring)
                if all(count <= 2 for count in a.values()):
                    curr = len(substring)
                    if curr > maxi:
                        maxi = curr
                else:
                    break 
        return maxi
