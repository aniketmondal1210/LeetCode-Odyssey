class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_list = list(set(nums))
        unique_list.sort(reverse = True)
        if len(unique_list) >= 3:
            return unique_list[2]
        else:
            return unique_list[0]
