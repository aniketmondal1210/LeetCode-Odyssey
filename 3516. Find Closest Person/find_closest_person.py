class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz_dist = abs(x-z)
        yz_dist = abs(y-z)
        if xz_dist > yz_dist:
            return 2
        elif xz_dist < yz_dist:
            return 1
        else:
            return 0
