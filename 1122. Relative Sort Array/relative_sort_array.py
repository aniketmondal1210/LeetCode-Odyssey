class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            result.extend([i] * arr1.count(i)) 
        rest = [j for j in arr1 if j not in arr2]
        return result + sorted(rest)
