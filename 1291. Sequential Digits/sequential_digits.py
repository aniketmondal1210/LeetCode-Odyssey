class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        a = len(str(low))
        b = len(str(high))
        for i in range(a,b+1):
            for j in range(0,len(digits)-i+1):
                num = int(digits[j:j+i])
                if low <= num <= high:
                    result.append(num)
        return result
