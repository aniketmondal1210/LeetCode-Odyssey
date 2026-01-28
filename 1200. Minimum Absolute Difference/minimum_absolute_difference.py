class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        mini = float('inf')
        for i in range(len(arr)-1):
            mini = min(abs(arr[i] - arr[i+1]),mini)
        for j in range(len(arr)-1):
            if abs(arr[j] - arr[j+1]) == mini:
                result.append([arr[j],arr[j+1]])
        return result
