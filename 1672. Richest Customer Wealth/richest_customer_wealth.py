class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            if sum > richest:
                richest = sum
        return richest
