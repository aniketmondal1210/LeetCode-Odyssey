class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = set(i*i for i in range(1,n+1))
        for i in range(1,n+1):
            for j in range(1,n+1):
                sum_sq = i**2 + j**2
                if sum_sq in squares:
                    count += 1
        return count
