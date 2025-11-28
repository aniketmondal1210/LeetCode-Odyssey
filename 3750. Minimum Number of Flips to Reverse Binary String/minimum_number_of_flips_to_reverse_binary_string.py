class Solution:
    def minimumFlips(self, n: int) -> int:
        a = bin(n)[2:]
        b = a[::-1]
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count
