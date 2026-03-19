class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (k & ~n) != 0:
            return -1
        a = bin(n)[2:]
        b = bin(k)[2:]
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        count = 0
        for i in range(max_len):
            if int(a[i]) ^ int(b[i]) == 1:
                count += 1
        return count
