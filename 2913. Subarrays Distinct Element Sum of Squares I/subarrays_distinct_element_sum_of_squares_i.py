class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        a = subarrays(nums)
        summ = 0
        for i in a:
            summ += len(set(i))**2
        return summ

def subarrays(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(arr[i:j+1])
    return result
