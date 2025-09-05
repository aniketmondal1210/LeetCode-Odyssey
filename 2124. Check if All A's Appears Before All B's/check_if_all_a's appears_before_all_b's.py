class Solution:
    def checkString(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i == 'a':
                new_s += i
        for j in s:
            if j == 'b':
                new_s += j
        return new_s == s
