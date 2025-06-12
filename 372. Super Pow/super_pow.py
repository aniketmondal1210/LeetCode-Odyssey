class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        exp_str = ""
        for i in b:
            exp_str += str(i)
        exp_int = int(exp_str)
        return pow(a,exp_int,1337)
