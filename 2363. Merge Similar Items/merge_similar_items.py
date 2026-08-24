class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        result = []
        a = [x[0] for x in items1]
        b = [x[0] for x in items2]
        for i in items1:
            if i[0] in b:
                result.append([i[0], i[1] + items2[b.index(i[0])][1]])
        for i in items2:
            if i[0] not in a:
                result.append(i)
        for i in items1:
            if i[0] not in b:
                result.append(i)
        result.sort()
        return result
