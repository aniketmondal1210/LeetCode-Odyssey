class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        new_num = num
        while(new_num != 0):
            if new_num % 2 == 0:
                new_num //= 2
                count += 1
            else:
                new_num -= 1
                count += 1
        return count
