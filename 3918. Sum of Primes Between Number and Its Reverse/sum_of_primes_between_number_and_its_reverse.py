class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = reverse(n)
        a = min(n, r)
        b = max(n, r)
        c = 0
        for i in range(a, b + 1):
            if is_prime(i):
                c += i
        return c

def reverse(x):
    return int(str(x)[::-1])

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
