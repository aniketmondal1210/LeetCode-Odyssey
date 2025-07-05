from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        a = Counter(arr)
        for key,value in a.items():
            if value > len(arr)//4:
                return key
