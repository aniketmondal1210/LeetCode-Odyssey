class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        summ = 0
        count = 0
        for i in costs:
            summ += i
            if summ > coins:
                return count
            count += 1
        return count
