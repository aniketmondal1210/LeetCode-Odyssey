class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        a = (5*n)//100
        return sum(arr[a:-a])/len(arr[a:-a])
