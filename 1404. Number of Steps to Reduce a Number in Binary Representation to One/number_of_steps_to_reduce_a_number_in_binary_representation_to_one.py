class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        a = int(s,2)
        while(a != 1 and a > 0):
            if a % 2 == 0:
                a //= 2
            else:
                a += 1
            count += 1
        return count
