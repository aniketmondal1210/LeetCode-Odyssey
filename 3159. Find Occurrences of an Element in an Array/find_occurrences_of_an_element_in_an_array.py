class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == x:
                result.append(i)
        ans = []
        for j in queries:
            if j - 1 < len(result):
                ans.append(result[j - 1])
            else:
                ans.append(-1)
        return ans
