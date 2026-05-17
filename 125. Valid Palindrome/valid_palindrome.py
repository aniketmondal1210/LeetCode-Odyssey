class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for i in s:
            if i.isalnum():
                cleaned_s += i
        cleaned_s = cleaned_s.lower()
        reversed_cleaned_s = cleaned_s[::-1]
        return reversed_cleaned_s == cleaned_s
