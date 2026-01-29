class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a = len(s) % k
        b = len(s) // k
        result = []
        for i in range(0,len(s),k):
            c = len(s[i:i+k])
            if c == k:
                result.append(s[i:i+k])
            else:
                result.append(s[i:i+k]+(k-c)*fill)
        return result
