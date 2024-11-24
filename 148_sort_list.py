from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        # Store head of new list
        dummy = ListNode(next=head)
        nextHead = head.next
        head.next = None

        # Probably need to input streaks of sorted node all at once like a zipper.
        while nextHead:
            head = nextHead
            nextHead = head.next
            head.next = None
            prev = dummy
            cur = dummy.next
            while cur:
                if cur.val > head.val:
                    prev.next = head
                    head.next = cur
                    break
                prev = cur
                cur = cur.next
            if not cur:
                prev.next = head
        return dummy.next
