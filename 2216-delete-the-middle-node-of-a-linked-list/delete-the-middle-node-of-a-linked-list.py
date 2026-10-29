# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        # n = 1: deleting the only node leaves an empty list
        if not head.next:
            return None

        slow = head
        fast = head.next.next  # fast leads by 2 so slow stops before the middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow.next is the middle node; skip over it
        slow.next = slow.next.next
        return head