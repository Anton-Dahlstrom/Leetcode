from typing import Optional

list1 = [1, 2, 4]
list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0)
        cur = first
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return first.next


ll1 = LinkedList()
ll2 = LinkedList()
for i in list1:
    ll1.insert_at_end(i)
for j in list2:
    ll2.insert_at_end(j)
ll1.print()
ll2.print()
obj = Solution()
result = obj.mergeTwoLists(ll1.head, ll2.head)
while result:
    print(result.val)
    result = result.next
