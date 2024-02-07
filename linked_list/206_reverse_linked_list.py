from typing import Optional

head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

# Definition for singly-linked list.


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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev = head
            head = prev.next
            prev.next = None
            while head:
                # print(prev.val)
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev.val


ll = LinkedList()
for i in head:
    ll.insert_at_end(i)
obj = Solution()
result = obj.reverseList(ll.head)
print(result)
