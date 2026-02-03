class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_dict = dict(zip(heights, names))
        sorted_heights = sorted(people_dict.keys(), reverse=True)
        result = [people_dict[height] for height in sorted_heights]
        return result
