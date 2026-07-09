# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        mid = self.length_ll(head)//2
        count = 0
        curr = head
        while count != mid:
            count += 1
            curr = curr.next
        return curr

    def length_ll(self,head):
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next
        return len
