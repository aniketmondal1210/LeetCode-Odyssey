class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_nums = [int(i) for i in nums]
        int_nums.sort()
        return str(int_nums[-k])
