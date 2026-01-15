class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = []
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                if len(s[i:j+1]) == 3:
                    result.append(s[i:j+1])
        count = 0
        for k in result:
            if len(set(k)) == 3:
                count += 1
        return count
