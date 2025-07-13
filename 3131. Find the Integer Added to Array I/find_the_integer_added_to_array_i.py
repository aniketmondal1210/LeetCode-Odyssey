class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        result = []
        x = min(nums2) - min(nums1)
        for i in range(len(nums1)):
            if x == nums2[i] - nums1[i]:
                result.append(x)   
        if len(set(result)) == 1:
            return x
        return -1   
