class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        new_str = ' '
        for i in words:
            if len(i) <= 2:
                new_str += i.lower() + ' '
            else:
                new_str += i.title() + ' '
        return new_str.strip()
            
