class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
        row2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        row3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        result = []
        for i in words:
            if all(j in row1 for j in i) or all(k in row2 for k in i) or all(l in row3 for l in i):
                result.append(i)
        return result
