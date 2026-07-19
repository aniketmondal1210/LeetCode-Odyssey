class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for char in s:
            if char == 'i':
                result = result[::-1]
            else:
                result.append(char)
        return "".join(result)
