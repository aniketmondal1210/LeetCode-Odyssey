class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        result = []
        for i in capacity:
            if i >= itemSize:
                result.append(i)
        if not result:
            return -1
        a = min(result)
        return capacity.index(a)©leetcode
