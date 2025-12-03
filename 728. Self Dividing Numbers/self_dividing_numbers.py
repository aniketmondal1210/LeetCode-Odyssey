class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for j in range(left,right+1):
            if self_dividing_number(j) == True:
                result.append(j)
        return result

def self_dividing_number(num):
    for i in str(num):
        if i == '0' or num % int(i) != 0:
            return False
    return True
