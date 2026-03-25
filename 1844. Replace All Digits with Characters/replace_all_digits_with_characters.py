class Solution:
    def replaceDigits(self, s: str) -> str:
        new_s = ""
        for i in range(len(s)):
            if s[i].isdigit():
                new_s += shift(s[i-1], int(s[i]))
            else:
                new_s += s[i]
        return new_s

def shift(letter, num):
    return chr(ord(letter) + num)
