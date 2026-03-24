class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []
        for i in s:
            if i.isalpha():
                letters.append(i)
        reversed_s = ""
        reversed_letters = letters[::-1]
        k = 0
        for j in s:
            if j.isalpha():
                reversed_s += reversed_letters[k]
                k += 1
            else:
                reversed_s += j
        return reversed_s
