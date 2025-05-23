class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            a = bin(i)[2:]
            result.append(no_of_ones(a))
        return result

def no_of_ones(n):
    count = 0
    for i in n:
        if i == '1':
            count += 1
    return count
