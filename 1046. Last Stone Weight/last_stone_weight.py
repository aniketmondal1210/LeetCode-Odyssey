class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort(reverse=True)
            a,b = stones[0],stones[1]
            if a == b:
                del stones[0:2]
            else:
                stones = stones[2:] + [abs(a-b)]
        return stones[0] if len(stones)>0 else 0
