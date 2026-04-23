class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for i in queries:
            found = False
            for j in dictionary:
                diff = 0
                for k in range(len(i)):
                    if i[k] != j[k]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    found = True
                    break
            if found:
                result.append(i)
        return result
