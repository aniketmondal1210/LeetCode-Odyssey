import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        for i in range(k):
            a = max(gifts)
            b = gifts.index(a)
            gifts[b] = math.floor(math.sqrt(a))
        return sum(gifts)
