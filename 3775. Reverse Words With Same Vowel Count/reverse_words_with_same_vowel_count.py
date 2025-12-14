class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        main_count = vowels_count(a[0])
        new_s = (a[0] + " ")
        for i in a[1:]:
            if vowels_count(i) == main_count:
                new_s += (i[::-1] + " ")
            else:
                new_s += (i + " ")
        return new_s.strip()

def vowels_count(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for j in word:
        if j in vowels:
            count += 1
    return count
