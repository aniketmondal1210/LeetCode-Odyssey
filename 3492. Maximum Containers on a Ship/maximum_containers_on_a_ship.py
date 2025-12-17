class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_containers = n*n
        no_of_containers = maxWeight // w
        return min(total_containers,no_of_containers)
