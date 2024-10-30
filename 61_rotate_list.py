from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not k or not head.next:
            return head

        tip = head
        i = 0
        while i < k:
            i += 1
            if tip.next:
                tip = tip.next
            else:
                tip = head
                k = k % i
                i = 0

        if head == tip:
            return head

        cur = head
        while tip.next:
            cur = cur.next
            tip = tip.next

        newHead = cur.next
        tip.next = head
        cur.next = None
        return newHead


head = [1, 2, 3, 4, 5]
k = 2
output = [4, 5, 1, 2, 3]


obj = Solution()
res = obj.rotateRight(head, k)
print(res)
print(output)
print(res == output)
