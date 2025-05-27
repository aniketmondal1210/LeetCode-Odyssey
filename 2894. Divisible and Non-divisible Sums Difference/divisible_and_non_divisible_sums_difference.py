class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr1 = []
        arr2 = []
        a = 0
        b = 0
        for i in range(1, n+1):
            if i%m == 0:
                arr2.append(i)
            else:
                arr1.append(i)
        a += sum(arr1)
        b += sum(arr2)
        return (a - b)
