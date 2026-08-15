class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        summ = requests[0]
        for i in range(1,len(requests)):
            summ += abs(requests[i] - requests[i-1])
        return summ
