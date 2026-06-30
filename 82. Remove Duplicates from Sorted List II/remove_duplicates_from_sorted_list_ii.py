from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        a = Counter(result)
        new_result = []
        for i in result:
            if a[i] == 1:
                new_result.append(i)
        return self.arr_to_ll(new_result)

    def arr_to_ll(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head
