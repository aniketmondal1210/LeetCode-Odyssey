class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        first = strs[0]
        for i in range(len(first)):
            ch = first[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return ans
            ans += ch
        return ans
