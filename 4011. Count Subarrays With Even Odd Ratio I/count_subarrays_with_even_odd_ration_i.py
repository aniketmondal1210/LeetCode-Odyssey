class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        count = 0
        for i in range(len(nums)):
            even_count = 0
            odd_count = 0
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                if odd_count > 0 and even_count * b <= odd_count * a:
                    count += 1
        return count
