text = ["LRUCache", "put", "put", "get",
        "put", "get", "put", "get", "get", "get"]
nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]


class LinkNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertAtEnd(self, node: LinkNode):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def insertBeginning(self, node: LinkNode):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def popNode(self, node: LinkNode):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
            node.prev = None
        if node.next:
            node.next.prev = node.prev
            node.next = None

    def print(self):
        cur = self.head
        while cur:
            print(f"key={cur.key} val={cur.val}")
            cur = cur.next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linklist = LinkList()
        self.keys = 0
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.linklist.popNode(node)
            self.linklist.insertBeginning(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.linklist.popNode(node)
            self.linklist.insertBeginning(node)
        else:
            if self.keys < self.capacity:
                self.keys += 1
                node = LinkNode(key, value)
                self.hmap[key] = node
                self.linklist.insertBeginning(node)
                # self.hmap[key] = LinkNode(key, value)
            else:
                node = LinkNode(key, value)
                self.linklist.insertBeginning(node)
                self.hmap[key] = node
                print(type(self.linklist.tail))
                removingNode = self.linklist.tail
                self.linklist.popNode(removingNode)
                self.hmap.pop(removingNode.key)
                self.linklist.print()


ll = LinkList()
node1 = LinkNode(1, 5)
node2 = LinkNode(2, 6)
node3 = LinkNode(3, 7)
ll.insertBeginning(node1)
ll.insertBeginning(node2)
ll.popNode(node2)
ll.insertBeginning(node3)
ll.print()


# lRUCache = LRUCache(nums[0])
