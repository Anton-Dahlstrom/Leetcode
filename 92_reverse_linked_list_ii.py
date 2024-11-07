from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        i = 1
        prev = None
        cur = head
        while i < left:
            prev = cur
            cur = cur.next
            i += 1

        leftHead = prev
        rightTail = cur

        while i <= right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp 
            i += 1

        leftTail = prev
        rightHead = cur
        
        rightTail.next = rightHead
        if leftHead:
            leftHead.next = leftTail
            return head
        return leftTail