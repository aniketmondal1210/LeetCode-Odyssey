class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        for i in range(1,int(n**0.5)+1):
            if n % i == 0:
                small.append(i)
                if i != (n//i):
                    large.append(n//i)
        result = small + large[::-1]
        if len(result) >= k:
            return result[k-1]
        else:
            return -1
