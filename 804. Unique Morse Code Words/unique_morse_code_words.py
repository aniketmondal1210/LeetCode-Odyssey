class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_alphabets = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        seen = set()
        for i in words:
            morse_word = ""
            for j in i:
                morse_word += morse_alphabets[ord(j) - ord('a')]
            seen.add(morse_word)
        return len(seen)
