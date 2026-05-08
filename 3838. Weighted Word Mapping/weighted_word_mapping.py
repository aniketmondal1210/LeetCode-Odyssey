class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        string = ""
        for i in words:
            summ = 0
            for j in i:
                summ += weights[weight_val(j) - 1]
            x = summ % 26
            string += reverse_weight_val(x)
        return string

def weight_val(char):
    return ord(char) - ord('a') + 1

def reverse_weight_val(num):
    return chr(ord('z') - num)
