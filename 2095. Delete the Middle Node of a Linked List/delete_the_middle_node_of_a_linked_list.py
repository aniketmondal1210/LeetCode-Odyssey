# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        length = length_ll(head)
        mid = length // 2 
        idx = 0
        current = head
        while idx != mid - 1:
            current = current.next
            idx += 1
        current.next = current.next.next
        return head

def length_ll(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next    
    return count
