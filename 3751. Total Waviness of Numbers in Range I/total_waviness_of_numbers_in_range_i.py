class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2 + 1):
            count += operation(i)
        return count


def operation(n):
    a = str(n)
    if len(a) < 3:
        return 0

    b = 0
    for i in range(1, len(a) - 1):
        left = int(a[i - 1])
        mid = int(a[i])
        right = int(a[i + 1])

        if mid > left and mid > right:
            b += 1
        elif mid < left and mid < right:
            b += 1
    return b
