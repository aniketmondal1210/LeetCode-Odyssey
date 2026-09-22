class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        num_set = set(nums)
        count = 0
        for x in nums:
            if (x - diff) in num_set and (x + diff) in num_set:
                count += 1
        return count
