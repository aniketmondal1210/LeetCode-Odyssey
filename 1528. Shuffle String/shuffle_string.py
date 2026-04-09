class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = [""] * len(s)
        for i,ch in enumerate(s):
            new_s[indices[i]] = s[i]
        return "".join(new_s)
