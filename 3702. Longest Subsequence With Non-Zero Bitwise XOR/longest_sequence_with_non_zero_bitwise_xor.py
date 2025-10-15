class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        result = nums 
        n = len(result)
        xor_all = 0
        for num in result:
            xor_all ^= num
        if xor_all != 0:
            return n
        else:
            has_non_zero = False
            for num in result:
                if num != 0:
                    has_non_zero = True
                    break
            if has_non_zero:
                return n - 1
            else:
                return 0
