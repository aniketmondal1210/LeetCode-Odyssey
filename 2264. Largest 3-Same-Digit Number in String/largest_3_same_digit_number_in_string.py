class Solution:
    def largestGoodInteger(self, num: str) -> str:
        three_digit_nos = ["000","111","222","333","444","555","666","777","888","999"]
        ans = "-1"
        ans_present = False
        for i in three_digit_nos:
            if i in num:
                if int(ans) <= int(i):
                    ans = i 
                    ans_present = True
        if ans_present == True:
            return ans
        return ""
