class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        count = 0
        for i in words:
            reversed_i = i[::-1]
            if reversed_i in seen:
                count += 1
            else:
                seen.add(i)
        return count
