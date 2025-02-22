class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            prev_num = 0
            curr_num = 1
            for i in range(2,n+1):
                next_num = prev_num + curr_num
                prev_num = curr_num
                curr_num = next_num
            return curr_num
