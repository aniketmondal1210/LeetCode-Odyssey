class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, n + 1):
            result.append(i)
        lex_sort = sorted(result,key = str)
        return lex_sort
