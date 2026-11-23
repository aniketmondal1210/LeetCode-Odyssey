class Solution:
    def assignUmbrella(self, rain):
        a = b = 0
        result = []
        for i in range(len(rain)):
            if rain[i] == 0:
                result.append("None")
            elif 0 <= i + 1 < len(rain) and rain[i + 1] == 1 and a <= b:
                result.append("Alice")
                a += 1
            else:
                result.append("Bob")
                b += 1
        return result
