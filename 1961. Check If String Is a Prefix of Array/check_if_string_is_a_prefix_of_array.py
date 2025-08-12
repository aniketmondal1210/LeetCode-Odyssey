class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        new_s = ""
        for i in words:
            new_s += i
            if new_s == s:
                return True
                break
        return False
