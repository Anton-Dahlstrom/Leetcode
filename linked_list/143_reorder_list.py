from typing import Optional

head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        first = head
        while head:
            array.append(head)
            head = head.next
        l = 0
        r = len(array)-1
        while l < r:
            array[l].next = array[r]
            array[r].next = array[l+1]
            l += 1
            r -= 1
        last = len(array)//2
        array[last].next = None
        return first


ll1 = LinkedList()
for i in head:
    ll1.insert_at_end(i)
ll1.print()
obj = Solution()
result = obj.reorderList(ll1.head)
while result:
    print(result.val)
    result = result.next
