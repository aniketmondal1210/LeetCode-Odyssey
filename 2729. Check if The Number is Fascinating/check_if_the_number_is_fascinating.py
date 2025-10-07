class Solution:
    def isFascinating(self, n: int) -> bool:
        string = str(n) + str(2*n) + str(3*n)
        numbers = ['1','2','3','4','5','6','7','8','9']
        string_numbers = list(string)
        string_numbers.sort()
        if numbers == string_numbers:
            return True
        return False
