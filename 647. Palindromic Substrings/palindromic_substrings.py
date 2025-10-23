class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if substring[::-1] == substring:
                    count += 1
        return count
