from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        i = 1
        while cur and i < left:
            cur = cur.next
            i += 1
        leftHead = cur
        dummy = ListNode()
        prev = dummy
        while cur and i < right:
            cur = cur.next
            cur.next = prev
            prev = cur
            i += 1
        leftHead.next = prev
