class Solution:
    def greatestLetter(self, s: str) -> str:
        a = list(set(s))
        maxi = 0
        for i in a:
            if i.lower() in s and i.upper() in s:
                maxi = max(maxi, ord(i.upper()))
        return chr(maxi).upper() if maxi != 0 else ""
