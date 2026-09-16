from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers_set = set(permutations(digits, 3))
        count = 0
        for i in numbers_set:
            if i[0] != 0 and i[2] % 2 == 0:
                count += 1
        return count
