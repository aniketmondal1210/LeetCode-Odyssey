class Solution:
    def BinarySearch(self, arr, l, r, tar):
        if l > r:
            return -1
        m = (l + r) // 2
        if arr[m] == tar:
            return m
        elif arr[m] > tar:
            return self.BinarySearch(arr, l, m - 1, tar)
        else:
            return self.BinarySearch(arr, m + 1, r, tar)

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        return self.BinarySearch(nums, start, end, target)
