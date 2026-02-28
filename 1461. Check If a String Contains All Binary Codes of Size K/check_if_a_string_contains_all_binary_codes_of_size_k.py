class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = substrs(s,k)
        return len(a) == 2**k

def substrs(p,l):
    seen = set()
    for i in range(len(p) - l + 1):
        seen.add(p[i:i+l])
    return seen
