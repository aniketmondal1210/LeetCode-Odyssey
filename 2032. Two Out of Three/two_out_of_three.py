class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2 or i in nums3:
                result.append(i)
        for j in nums2:
            if j in nums3 or j in nums1:
                result.append(j)
        for k in nums3:
            if k in nums1 or k in nums2:
                result.append(k)
        return list(set(result))
