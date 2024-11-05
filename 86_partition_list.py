from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyLarge = ListNode()
        dummySmall = ListNode()
        curLarge = dummyLarge 
        curSmall = dummySmall 
        cur = head
        while cur:
            if cur.val < x:
                curSmall.next = cur
                curSmall = cur
            else:
                curLarge.next = cur
                curLarge = cur
            prev = cur
            cur = cur.next
            prev.next = None
        curSmall.next = dummyLarge.next

        if dummySmall.next:
            return dummySmall.next
        return dummyLarge.next