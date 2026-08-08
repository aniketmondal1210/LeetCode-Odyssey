class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        dictionary = {}
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_index = 0
        for i in key:
            if i not in dictionary:
                dictionary[i] = alphabets[alphabet_index]
                alphabet_index += 1
        result = ""
        for i in message:
            if i == " ":
                result += " "
            else:
                result += dictionary[i]
        return result
