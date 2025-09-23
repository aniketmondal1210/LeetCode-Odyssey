class Solution:
    def stringHash(self, s: str, k: int) -> str:
        new_str = ""
        for j in range(0, len(s), k):
            substring = s[j:j + k]
            hash_value = sum(ord(char) - ord('a') for char in substring) % 26
            new_str += chr(hash_value + ord('a'))
        return new_str
