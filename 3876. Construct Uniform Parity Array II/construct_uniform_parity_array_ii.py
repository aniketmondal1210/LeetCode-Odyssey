class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        if mini % 2 == 1:
            return True
        else:
            for num in nums1:
                if num % 2 == 1:
                    return False
            return True

# Even - Even = Even
# Odd - Odd = Even  
# Even - Odd = Odd
# Odd - Even = Odd
