class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        mul = 1

        while(n > 0):
            digit = n % 10
            if digit != 0:
                result.append(digit*mul)
            mul *= 10
            n //= 10
        
        return result[::-1]
