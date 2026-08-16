class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        result = {}
        for i in range(len(drones)):
            dist = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if dist <= drones[i][2]:
                result[i] = dist
        if not result:
            return -1
        a = min(result.values())
        for key,value in result.items():
            if value == a:
                return key
