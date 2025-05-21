class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num_odds = 0
        for i in arr:
            if i % 2 == 0:
                num_odds = 0
            else:
                num_odds += 1
                if num_odds == 3: return True
        return False
