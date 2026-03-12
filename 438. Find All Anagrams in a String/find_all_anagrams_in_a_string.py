class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_sorted = "".join(sorted(p))
        for i in range(len(s)-len(p)+1):
            if "".join(sorted(s[i:i+len(p)])) == p_sorted:
                result.append(i)
        return result
