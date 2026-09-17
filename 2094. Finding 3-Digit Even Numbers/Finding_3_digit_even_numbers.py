from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        a = permutations(digits, 3)
        result_set = set()
        for i in a:
            if i[0] != 0:
                number = i[0] * 100 + i[1] * 10 + i[2]
                if number % 2 == 0:
                    result_set.add(number)
        return sorted(list(result_set))
