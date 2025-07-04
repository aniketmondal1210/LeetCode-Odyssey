class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        a = Counter(arr[::-1])
        for key,value in a.items():
            if key == value:
                return key
            
        return -1
