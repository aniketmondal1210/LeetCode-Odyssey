from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        for i in count1.keys():
            min_count = min(nums1.count(i), nums2.count(i))
            result.extend([i] * min_count)
        return result
