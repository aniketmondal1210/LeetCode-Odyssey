class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstWordValue = int("".join([str(ord(i)-ord('a')) for i in firstWord]))
        secondWordValue = int("".join([str(ord(i)-ord('a')) for i in secondWord]))
        targetWordValue = int("".join([str(ord(i)-ord('a')) for i in targetWord]))
        return (firstWordValue + secondWordValue == targetWordValue) or (firstWordValue + targetWordValue == secondWordValue) or (targetWordValue + secondWordValue == firstWordValue)
