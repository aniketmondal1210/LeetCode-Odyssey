class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        result = ""
        for i in words:
            if i[::-1] == i:
                result += i
                break
        return result
