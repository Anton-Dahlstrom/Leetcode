from typing import Optional

head = [1, 2, 3, 4, 5]
n = 2
# Output: [1, 2, 3, 5]

head = [1, 2]
n = 1
# Output: [1]

head = [1]
n = 1
# Output: []

head = [1, 2]
n = 2
# Output: [2]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, array):
        for value in array:
            if self.head:
                self.head = ListNode(value, self.head)
            else:
                self.head = ListNode(value)

    def insert_at_beginning(self, data):
        node = ListNode(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = ListNode(data, None)

    def print(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.val) + "-->"
            itr = itr.next
        print(llstr)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        l = head
        prev = None
        cur = head
        while cur:
            cur = cur.next
            count += 1
            if count > n:
                prev = l
                l = l.next
        if count < 2:
            return None
        if l and prev:
            prev.next = l.next
        elif l:
            return l.next
        return head


ll1 = LinkedList()
for i in head:
    ll1.insert_at_end(i)
ll1.print()
obj = Solution()
result = obj.removeNthFromEnd(ll1.head, n)
while result:
    print(result.val)
    result = result.next
