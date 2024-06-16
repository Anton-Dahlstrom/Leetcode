from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = None
        count = 0
        cur = head
        left = head
        right = None
        while cur:
            count += 1
            if count == k-1:
                mid = cur
            if count == 1:
                left = cur
            elif count == k:
                if not root:
                    root = cur
                curNext = cur.next
                leftNext = left.next

                if k > 2:
                    left.next = curNext
                    cur.next = leftNext
                    mid.next = left
                else:
                    left.next = cur.next
                    cur.next = left
                if right:
                    right.next = cur
                cur = left
                right = cur
                count = 0
            cur = cur.next

        if root:
            return root
        return head


head = [1, 2, 3, 4, 5]
k = 2

head = [1, 2, 3, 4]
k = 4

nodes = list(map(ListNode, head))
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
root = nodes[0]

obj = Solution()
res = obj.reverseKGroup(root, k)
cur = res

count = 0
while cur:
    print(cur.val)
    cur = cur.next
    count += 1
    if count > len(nodes):
        print("looping")
        break
