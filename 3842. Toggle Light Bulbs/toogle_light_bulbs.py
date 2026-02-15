class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulbs_set = set(bulbs)
        bulbs_on = [i for i in bulbs_set if bulbs.count(i) % 2 == 1]
        return sorted(bulbs_on)
