class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        a = bin(n)[2:]
        count = 0
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i+1] == '1':
                count += 1
        return count == 1
