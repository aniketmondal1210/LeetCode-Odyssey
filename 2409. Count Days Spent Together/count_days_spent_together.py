class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def dateToDayNumber(dateStr):
            month = int(dateStr[:2])
            day = int(dateStr[3:])
            totalDays = 0
            for i in range(month - 1):
                totalDays += days[i]
            totalDays += day
            return totalDays
        aliceStart = dateToDayNumber(arriveAlice)
        aliceEnd = dateToDayNumber(leaveAlice)
        bobStart = dateToDayNumber(arriveBob)
        bobEnd = dateToDayNumber(leaveBob)
        latestStart = max(aliceStart, bobStart)
        earliestEnd = min(aliceEnd, bobEnd)
        overlapDays = earliestEnd - latestStart + 1
        if overlapDays < 0:
            return 0    
        return overlapDays
