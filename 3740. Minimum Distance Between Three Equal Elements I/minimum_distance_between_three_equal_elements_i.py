class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        a = set(nums)
        result = []
        for i in a:
            if nums.count(i) >= 3:
                result.append(i)
        dist = float('inf')
        for j in result:
            occurrence = []
            for k in range(len(nums)):
                if nums[k] == j:
                    occurrence.append(k)
            for l in range(len(occurrence)-2):
                x = occurrence[l]
                y = occurrence[l+1]
                z = occurrence[l+2]
                distance = abs(x-y) + abs(y-z) + abs(z-x)
                dist = min(distance, dist)
        return dist if dist != float('inf') else -1



from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        min_distance = float('inf')
        for num, index in index_map.items():
            if len(index) >= 3:
                for i in range(len(index) - 2):
                    a, b, c = index[i], index[i+1], index[i+2]
                    distance = abs(a-b) + abs(b-c) + abs(c-a)
                    min_distance = min(min_distance, distance)
        return min_distance if min_distance != float('inf') else -1
