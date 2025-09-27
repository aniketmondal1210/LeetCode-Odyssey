class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs(30*hour - 5.5*minutes)
        return a if a < 360 - a else 360 - a
