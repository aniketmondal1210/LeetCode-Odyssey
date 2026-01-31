class Solution:
    def reverseByType(self, s: str) -> str:
        letter = []
        character = []
        reversed_s = ''
        for i in s:
            if i.isalpha():
                letter.append(i)
            else:
                character.append(i)
        letter = letter[::-1]
        character = character[::-1]
        for j in s:
            if j.isalpha():
                reversed_s += letter.pop(0)
            else:
                reversed_s += character.pop(0)
        return reversed_s©leetcode
