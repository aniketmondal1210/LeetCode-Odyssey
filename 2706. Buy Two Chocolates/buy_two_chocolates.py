class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum = prices[0]+prices[1]
        if sum <= money:
            return money - sum
        return money
