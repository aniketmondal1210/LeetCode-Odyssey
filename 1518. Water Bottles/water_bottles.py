class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        summ = numBottles
        while(numBottles >= numExchange):
            exchanged = numBottles // numExchange
            summ += exchanged
            numBottles = exchanged + (numBottles % numExchange)
        return summ
