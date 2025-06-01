class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        for i in nums:
            if len(str(i)) == 1:
                single_sum += i
            else:
                double_sum += i
        if single_sum > double_sum or double_sum > single_sum:
            return True
        else:
            return False
