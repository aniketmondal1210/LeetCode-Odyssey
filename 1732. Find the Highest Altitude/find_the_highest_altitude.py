class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        summ = 0
        for i in gain:
            summ += i
            if summ > maxi:
                maxi = summ
        return maxi
