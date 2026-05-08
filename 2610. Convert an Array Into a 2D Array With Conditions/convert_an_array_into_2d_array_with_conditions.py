class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = 0
        n = len(nums)
        while count != n:
            seen = set()
            row = []
            for i in range(len(nums)):
                if nums[i] is not None and nums[i] not in seen:
                    seen.add(nums[i])
                    row.append(nums[i])
                    nums[i] = None
                    count += 1
            result.append(row)
        return result
