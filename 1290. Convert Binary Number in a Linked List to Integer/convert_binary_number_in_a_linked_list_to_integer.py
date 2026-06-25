# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        a = "".join(str(i) for i in result)
        return int(a,2)
