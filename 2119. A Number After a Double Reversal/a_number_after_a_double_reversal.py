class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        else:
            a = str(num)[::-1]
            a = a.lstrip('0')
            b = a[::-1]
            if int(b) == num:
                return True
            return False
