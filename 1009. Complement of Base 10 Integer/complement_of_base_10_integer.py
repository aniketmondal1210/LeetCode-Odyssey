class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)[2:]
        result = ""
        for i in a:
            if i == '1':
                result += '0'
            else:
                result += '1'
        return int(result,2)
