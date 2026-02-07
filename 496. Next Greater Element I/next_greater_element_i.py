class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            pos = nums2.index(i)
            next_greater = -1
            for j in range(pos+1,len(nums2)):
                if nums2[j] > i:
                    next_greater = nums2[j]
                    break
            result.append(next_greater)
        return result
