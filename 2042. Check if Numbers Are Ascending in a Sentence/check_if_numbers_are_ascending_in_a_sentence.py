class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        numbers = []
        for word in words:
            if word.isdigit():
                numbers.append(int(word))
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i + 1]:
                return False
                break
        return True
