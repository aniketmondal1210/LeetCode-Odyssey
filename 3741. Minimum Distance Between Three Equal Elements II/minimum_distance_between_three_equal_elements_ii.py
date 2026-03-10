from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        min_distance = float('inf')
        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    a = indices[i]
                    c = indices[i+2]
                    distance = 2 * (c - a)
                    min_distance = min(min_distance, distance)
        return min_distance if min_distance != float('inf') else -1
