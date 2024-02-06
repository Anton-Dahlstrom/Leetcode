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

    def insert_at_beginning(self, data):
        node = ListNode(data, self.head)
        self.head = node

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
        head.reverse()
        return head


ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(25)
ll.print()

# obj = Solution()
# result = obj.reverseList(head)
# print(result)
