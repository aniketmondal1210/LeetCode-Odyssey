class Solution:
    def largestInteger(self, num: int) -> int:
        odd_nums = []
        even_nums = []
        for i in str(num):
            if int(i) % 2 == 0:
                even_nums.append(int(i))
            else:
                odd_nums.append(int(i))
        odd_nums.sort(reverse=True)
        even_nums.sort(reverse=True)
        result = []
        odd_idx = 0
        even_idx = 0
        for i in str(num):
            digit = int(i)
            if digit % 2 == 0:
                result.append(str(even_nums[even_idx]))
                even_idx += 1
            else:
                result.append(str(odd_nums[odd_idx]))
                odd_idx += 1
        return int("".join(result))
