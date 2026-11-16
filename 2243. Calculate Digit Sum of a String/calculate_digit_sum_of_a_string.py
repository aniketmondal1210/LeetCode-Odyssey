class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = []
            for i in range(0, len(s), k):
                summ = 0
                for j in range(i, min(i + k, len(s))):
                    summ += int(s[j])
                result.append(str(summ))
            s = "".join(result)
        return s
