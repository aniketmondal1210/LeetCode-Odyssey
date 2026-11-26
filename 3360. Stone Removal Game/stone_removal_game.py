class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        x = 10
        while n >= x:
            n -= x
            x -= 1
            alice_turn = not alice_turn
        return not alice_turn
