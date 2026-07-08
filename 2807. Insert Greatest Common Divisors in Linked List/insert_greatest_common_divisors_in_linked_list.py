# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            a = curr.val
            b = curr.next.val
            c = math.gcd(a, b)
            next_node = curr.next
            gcd_node = ListNode(c)
            curr.next = gcd_node
            gcd_node.next = next_node
            curr = next_node
        return head
