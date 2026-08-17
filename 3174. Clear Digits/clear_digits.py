class Solution:
    def clearDigits(self, s: str) -> str:
        a = []
        for i in s:
            if i.isdigit():
                a.pop()
            else:
                a.append(i)
        return "".join(a)
