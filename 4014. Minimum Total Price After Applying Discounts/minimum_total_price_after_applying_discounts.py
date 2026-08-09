class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        result = 0.0
        a = len(prices)
        b = len(discounts)
        for i in range(min(a, b)):
            discounted_price = prices[i] * (100 - discounts[i]) / 100
            result += discounted_price
        for i in range(min(a, b), a):
            result += prices[i]
        return result
