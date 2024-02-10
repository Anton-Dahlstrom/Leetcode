from typing import Optional

head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self):
        self.head = None

    def makeList(self, array):
        stack = []
        for node in array:
            stack.append(Node(node[0]))
        for i in range(0, len(stack)):
            if i < len(stack)-1:
                stack[i].next = stack[i+1]
            if array[i][1] != None:
                stack[i].random = stack[array[i][1]]
        self.head = stack[0]

    def print(self):
        cur = self.head
        while cur:
            pstr = str(cur.val)
            if cur.random:
                pstr += " " + str(cur.random.val)
            print(pstr)
            cur = cur.next

# First we iterate through the linked list and assign an index to each node and create an array of node copies and assign them the value of their corresponding original node.
# We then iterate through the original nodes and assign the corresponding node copy in the array it's .next and .random based on the indexes of the nodes the original node points to.
# In short: 1. Assign index to old nodes and make array of new nodes
#           2. Iterate through original and copy nodes and assign the copy nodes .next and .random attribute based on what index we find in the .next and .random attributes of the
#              original node.


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(1)
        prev = dummy
        cur = head
        count = 1
        array = [dummy]
        while cur:
            prev.next = cur
            prev = cur
            cur.index = count
            array.append(Node(cur.val))
            cur = cur.next
            count += 1
        count = 1
        cur = head
        while cur:
            if cur.random:
                array[count].random = array[cur.random.index]
            if count < len(array)-1:
                array[count].next = array[count+1]
            cur = cur.next
            count += 1

        return array[1]


ll1 = LinkedList()
ll1.makeList(head)
# ll1.print()
obj = Solution()
result = obj.copyRandomList(ll1.head)
while result:
    pstr = str(result.val)
    if result.random:
        pstr += " " + str(result.random.val)
    print(pstr)
    result = result.next

# class Tester:
#     def __init__(self) -> None:
#         self.test = 1
#         self.two = 2


# obj = Tester()
# obj.three = 3
# print(obj.three)
