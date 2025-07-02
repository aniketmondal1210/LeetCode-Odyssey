class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        flag = True
        if len(arr) > 2:
            for i in range(len(arr)-1):
                diff = arr[0] - arr[1]
                if arr[i] - arr[i+1] != diff:
                    flag = False
        return flag
