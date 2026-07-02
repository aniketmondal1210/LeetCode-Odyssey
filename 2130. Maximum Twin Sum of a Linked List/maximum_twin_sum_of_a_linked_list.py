# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        maxi = 0
        n = len(result)
        for i in range(n // 2):
            maxi = max(maxi, result[i] + result[n - 1 - i])
        return maxi
