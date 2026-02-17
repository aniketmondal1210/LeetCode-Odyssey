class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if self.isPrime(i):
                result.append(i)
        
        if len(result) < 2:
            return [-1, -1]
        
        mini = float('inf')
        min_arr = []
        for j in range(len(result)-1):
            if result[j+1] - result[j] < mini:
                mini = result[j+1] - result[j]
                min_arr = [result[j], result[j+1]]
                
        return min_arr
    
    def isPrime(self, n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for k in range(3, int(n**0.5) + 1, 2):
                if n % k == 0:
                    return False
        return True
