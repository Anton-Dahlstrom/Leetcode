from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        node = head.next
        head.next = None
        i = 0
        while node:
            temp = node.next
            prev = dummy
            cur = dummy.next
            while cur and node.val > cur.val:
                prev = cur
                cur = cur.next
            prev.next = node
            node.next = cur
            node = temp 

        return dummy.next


head = [4,2,1,3]
output = [1,2,3,4]

dummy = ListNode()
prev = dummy 
for val in head:
    cur = ListNode(val)
    prev.next = cur
    prev = cur

obj = Solution()
cur = obj.insertionSortList(dummy.next)
res = []
while cur:
    res.append(cur.val)
    cur = cur.next
print(res)
print(output)
print(res == output)