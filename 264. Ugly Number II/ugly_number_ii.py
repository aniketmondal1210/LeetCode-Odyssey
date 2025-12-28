class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        iTwo = 0
        iThree = 0
        iFive = 0
        for i in range(n-1):
            two = ugly[iTwo] * 2
            three = ugly[iThree] * 3
            five = ugly[iFive] * 5
            nextUgly = min(two, three, five)
            ugly.append(nextUgly)
            if nextUgly == two:
                iTwo += 1
            if nextUgly == three:
                iThree += 1
            if nextUgly == five:
                iFive += 1
        return ugly[-1]
