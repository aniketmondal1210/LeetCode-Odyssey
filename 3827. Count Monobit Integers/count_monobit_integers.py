class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(0, n + 1):
            binary = bin(i)[2:]
            if binary.count('1') == len(binary) or binary.count('0') == len(binary):
                count += 1
        return count
