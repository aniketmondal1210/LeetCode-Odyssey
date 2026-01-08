class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if len(set(nums1).intersection(set(nums2))) > 0:
            return min(set(nums1).intersection(set(nums2)))
        else:
            nums1_min = min(nums1)
            nums2_min = min(nums2)
            a = int(str(nums1_min) + str(nums2_min))
            b = int(str(nums2_min) + str(nums1_min))
            return a if b > a else b
