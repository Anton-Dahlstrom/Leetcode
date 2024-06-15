from typing import List, Optional
import heapq

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MinHeapNodes:
    def heapify(self, array: list):
        for i in reversed(range(0, len(array))):
            self.siftup(array, i)

    def push(self, array: list, node: ListNode):
        array.append(node)
        self.siftup(array, len(array)-1)

    def pop(self, array: list, index: int):
        if len(array) < 2:
            return array.pop()
        array[index], array[-1] = array[-1], array[index]
        node = array.pop()
        cur = index
        child1 = (cur * 2) + 1
        child2 = (cur * 1) + 2
        while child1 < len(array):
            if child2 >= len(array) or array[child1].val < array[child2].val:
                if array[cur].val < array[child1].val:
                    break
                array[cur], array[child1] = array[child1], array[cur]
                cur = child1
            else:
                if array[cur].val < array[child2].val:
                    break
                array[cur], array[child2] = array[child2], array[cur]
                cur = child2
            child1 = (cur * 2) + 1
            child2 = (cur * 2) + 2
        return node

    def siftup(self, array, index):
        cur = index
        parent = (cur - 1)//2
        while array[cur].val < array[parent].val and parent >= 0:
            array[cur], array[parent] = array[parent], array[cur]
            cur = parent
            parent = (cur - 1)//2


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        nodes = []
        heap = MinHeapNodes()
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heap.push(nodes, lists[i])
        if not nodes:
            return None
        root = heap.pop(nodes, 0)
        if root.next:
            heap.push(nodes, root.next)
        cur = root
        while nodes:
            cur.next = heap.pop(nodes, 0)
            cur = cur.next
            if cur.next:
                heap.push(nodes, cur.next)
        return root


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output = [1, 1, 2, 3, 4, 4, 5, 6]

lists = [[-3, 2, 2], [-9], [-10, -5, -4, -2, -1, 1, 3, 4],
         [-10, -9, -8, 3, 4], [-5, -3, 3, 4], [-9, -8, -5, -4, -2, -1, 3]]

Output = [-10, -10, -9, -9, -9, -8, -8, -5, -5, -5, -4, -
          4, -3, -3, -2, -2, -1, -1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4]

nodes = []
for arr in lists:
    if arr[0]:
        cur = ListNode(arr[0])
        nodes.append(cur)
        for val in arr[1:]:
            cur.next = ListNode(val)
            cur = cur.next

obj = Solution()
res = obj.mergeKLists(nodes)
reslist = []

while res:
    reslist.append(res.val)
    res = res.next
print(reslist)
print(Output)
print(reslist == Output)
