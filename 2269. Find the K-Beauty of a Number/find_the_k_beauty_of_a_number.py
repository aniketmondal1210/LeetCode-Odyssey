class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)
        for i in range(len(num_str) - k + 1):
            sub_num = int(num_str[i:i+k])
            if sub_num != 0 and num % sub_num == 0:
                count += 1
        return count
