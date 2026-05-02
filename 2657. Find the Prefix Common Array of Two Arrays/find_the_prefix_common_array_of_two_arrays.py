class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()
        result = []
        for i in range(len(A)):
            seen_A.add(A[i])
            seen_B.add(B[i])
            result.append(len(seen_A & seen_B))
        return result
