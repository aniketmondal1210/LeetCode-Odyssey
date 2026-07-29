class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = []
        for num in range(lo, hi + 1):
            curr = num
            count = 0
            while curr != 1:
                if curr % 2 == 0:
                    curr //= 2
                else:
                    curr = 3 * curr + 1
                count += 1
            result.append((count, num))   
        result.sort()
        return result[k - 1][1]
