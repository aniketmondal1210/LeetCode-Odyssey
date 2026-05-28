class Solution:
    def passwordStrength(self, password: str) -> int:
        summ = 0
        special = {'!', '@', '#', '$'}
        set_password = set(password)
        for i in set_password:
            if 'a' <= i <= 'z':
                summ += 1
            elif 'A' <= i <= 'Z':
                summ += 2
            elif '0' <= i <= '9':
                summ += 3
            elif i in special:
                summ += 5
        return summ
