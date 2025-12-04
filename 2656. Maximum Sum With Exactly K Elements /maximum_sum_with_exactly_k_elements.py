class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        for i in range(k):
            a = nums[-1]
            result += a
            nums.pop()
            nums.append(a+1)
        return result
