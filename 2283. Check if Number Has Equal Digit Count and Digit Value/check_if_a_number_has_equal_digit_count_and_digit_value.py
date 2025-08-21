class Solution:
    def digitCount(self, num: str) -> bool:
        flag = False
        for i in range(len(num)):
            if num.count(str(i)) == int(num[i]):
                flag = True
            else:
                flag = False
                break
        return flag
