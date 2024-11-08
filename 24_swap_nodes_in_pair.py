from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy = ListNode(next=head) 
        prev = dummy
        while cur and cur.next:
            nextNode = cur.next
            prev.next = nextNode 
            cur.next = nextNode.next 
            nextNode.next = cur
            prev = cur 
            cur = cur.next 
        return dummy.next