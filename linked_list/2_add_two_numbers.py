from typing import Optional

l1 = [2, 4, 3]
l2 = [5, 6, 4]
# Output: [7,0,8]


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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        sum = 0
        while l1:
            sum += l1.val * multiplier
            l1 = l1.next
            multiplier *= 10
        multiplier = 1
        while l2:
            sum += l2.val * multiplier
            l2 = l2.next
            multiplier *= 10
        dummy = ListNode()
        prev = dummy
        for char in reversed(str(sum)):
            cur = ListNode(int(char))
            prev.next = cur
            prev = cur
            cur = cur.next
        return dummy.next


ll1 = LinkedList()
ll2 = LinkedList()
for i in l1:
    ll1.insert_at_end(i)
for j in l2:
    ll2.insert_at_end(j)
ll1.print()
obj = Solution()
result = obj.addTwoNumbers(ll1.head, ll2.head)
while result:
    print(result.val)
    result = result.next
