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
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        arr.sort(key=lambda n: n.val)
        arr.append(None)
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        return arr[0]
