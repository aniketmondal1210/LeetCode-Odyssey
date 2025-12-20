class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]

        if leap_year(int(date[:4])) and months[1] == 28:
            months[1] = 29
                    
        month = int(date[5:7])
        month_days = sum(i for i in months[:month-1])
        days = int(date[8:])
        
        return month_days + days

def leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
