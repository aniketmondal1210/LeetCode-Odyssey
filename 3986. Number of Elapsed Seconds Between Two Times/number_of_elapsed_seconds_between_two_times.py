class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start_h = int(startTime[0:2])
        start_m = int(startTime[3:5])
        start_s = int(startTime[6:8])
        end_h = int(endTime[0:2])
        end_m = int(endTime[3:5])
        end_s = int(endTime[6:8])
        start_total = start_h * 3600 + start_m * 60 + start_s
        end_total = end_h * 3600 + end_m * 60 + end_s
        return end_total - start_total
