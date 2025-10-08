class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount
        else:
            lower = (purchaseAmount // 10) * 10
            upper = lower + 10
            mid = (lower + upper) // 2
            if purchaseAmount >= mid:
                return 100 - upper
            else:
                return 100 - lower
