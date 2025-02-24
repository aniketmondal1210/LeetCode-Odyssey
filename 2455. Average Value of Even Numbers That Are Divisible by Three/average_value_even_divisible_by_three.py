class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum = 0
        count = 0
        for i in nums:
            if(i%2==0 and i%3 == 0):
                sum+=i
                count+=1
        if(count==0):
            return 0
        else:
            return sum//count
