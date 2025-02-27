class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        required_words = words[:k]
        return ' '.join(required_words)
