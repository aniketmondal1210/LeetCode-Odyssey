class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        a = set(nums1).intersection(set(nums2))
        return min(list(a)) if len(a) > 0 else -1
