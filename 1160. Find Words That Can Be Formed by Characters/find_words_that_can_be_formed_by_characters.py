from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        a = Counter(chars)
        result = 0
        for i in words:
            b = Counter(i)
            flag = True
            for char, count in b.items():
                if a[char] < count:
                    flag = False
                    break
            if flag:
                result += len(i)
        return result
