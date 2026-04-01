class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_list1 = list(s1)
        s1_list1[0], s1_list1[2] = s1_list1[2], s1_list1[0]
        a = ''.join(s1_list1)
        s1_list2 = list(s1)
        s1_list2[1], s1_list2[3] = s1_list2[3], s1_list2[1]
        b = ''.join(s1_list2)
        s1_list3 = list(s1)
        s1_list3[0], s1_list3[2] = s1_list3[2], s1_list3[0]
        s1_list3[1], s1_list3[3] = s1_list3[3], s1_list3[1]
        c = ''.join(s1_list3)
        return a == s2 or b == s2 or c == s2
