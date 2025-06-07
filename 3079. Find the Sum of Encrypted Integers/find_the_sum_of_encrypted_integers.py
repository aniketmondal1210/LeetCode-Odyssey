class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            result.append(int(encryptNum(num)))
        return sum(result)



def encryptNum(n):
    max_digit = 0
    for i in str(n):
        if int(i) > max_digit:
            max_digit = int(i)
    return str(max_digit) * len(str(n))
