class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R_count = 0
        L_count = 0
        count = 0
        for i in s:
            if i == 'R':
                R_count += 1
            else:
                L_count += 1
            if R_count == L_count:
                count += 1
        return count
