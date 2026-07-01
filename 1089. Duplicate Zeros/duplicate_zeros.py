class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if all(i == 0 for i in arr):
            return arr
        elif all(i != 0 for i in arr):
            return arr
        else:
            result = []
            for j in arr:
                result.append(j)
                if j == 0:
                    result.append(0)
            for k in range(len(arr)):
                arr[k] = result[k]
