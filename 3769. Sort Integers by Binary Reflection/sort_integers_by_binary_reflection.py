class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            a = bin(nums[i])[2:]
            b = a[::-1]
            c = int(b,2)
            result.append((c,nums[i]))
        d = sorted(result)
        return [j[1] for j in d]
