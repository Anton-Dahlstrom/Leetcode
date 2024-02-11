from typing import Optional

head = [3, 2, 0, -4]
pos = 1
Output: True

head = [1]
pos = -1
Output: False


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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        hmap = {}
        while cur:
            if cur in hmap:
                print(hmap)
                return True
            else:
                hmap[cur] = 1
            cur = cur.next
        return False


ll1 = LinkedList()
for i in head:
    ll1.insert_at_end(i)
ll1.print()
obj = Solution()
result = obj.hasCycle(ll1.head)
print(result)
