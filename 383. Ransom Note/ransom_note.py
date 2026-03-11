from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for char in r_count:
            if m_count[char] < r_count[char]:
                return False
        return True
