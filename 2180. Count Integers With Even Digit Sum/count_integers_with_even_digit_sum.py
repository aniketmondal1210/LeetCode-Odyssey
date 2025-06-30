class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2,num+1):
            if digit_sum(i) % 2 == 0:
                count += 1
        return count


def digit_sum(n):
    summ = 0
    for j in str(n):
        summ += int(j)
    return summ
