from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        root = None
        count = 0
        cur = head
        nodes = []
        # The tail of the previously reversed group of nodes need to point to the new head of the
        # next group of reversed nodes.
        lastTail = None
        while cur:
            count += 1
            nodes.append(cur)
            if count == k:
                if not root:
                    root = cur
                tempnext = cur.next
                for i in reversed(range(1, len(nodes))):
                    print(len(nodes), i)
                    nodes[i].next = nodes[i-1]
                if lastTail:
                    lastTail.next = cur
                lastTail = nodes[0]
                cur = nodes[0]
                cur.next = tempnext
                nodes = []
                count = 0
            cur = cur.next

        if root:
            return root
        return head


head = [1, 2, 3, 4, 5]
k = 2

# head = [1, 2, 3, 4]
# k = 4

# head = [1, 2, 3, 4, 5]
# k = 1

head = [1, 2, 3, 4, 5, 6]
k = 2

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
