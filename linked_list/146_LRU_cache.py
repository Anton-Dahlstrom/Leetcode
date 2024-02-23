text = ["LRUCache", "put", "put", "get",
        "put", "get", "put", "get", "get", "get"]
nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

text = ["LRUCache",
        "put", "put", "put",
        "put", "get", "get",
        "get", "get", "put",
        "get", "get", "get",
        "get", "get"]
nums = [[3],
        [1, 1], [2, 2], [3, 3],
        [4, 4], [4], [3],
        [2], [1], [5, 5],
        [1], [2], [3],
        [4], [5]]


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
        if node == None:
            print("insert node is none")
        if not self.head:
            self.head = node
            self.tail = node
            # node.prev = node
            # node.next = node
            return
        if self.tail == None:
            print("here tail is None")
            cur = self.head
            while cur:
                print(cur.val)
                cur = cur.next
            print("end of print")
        self.head.prev = node
        node.next = self.head
        self.head = node

    def popNode(self, node: LinkNode):
        if node == None:
            print("node is none")
            return
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            print("THIS IS NODE.PREV", node.prev)
            self.tail = node.prev

        if node.prev is not None:
            print("test", node.key)
            node.prev.next = node.next
            print("test2", node.key)
            node.prev = None
        if node.next is not None:
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
        if self.linklist.head:
            print("linklist vals get")
            print(key)
            print(self.linklist.head.key)
            print(self.linklist.tail.key)
            print("stopping")
            print(self.hmap)
        if key in self.hmap:
            node = self.hmap[key]
            self.linklist.popNode(node)
            self.linklist.insertBeginning(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.linklist.head:
            print(key, value)
            print("linklist vals put")
            print(self.linklist.head.key)
            print(self.linklist.tail.key)
            print("stopping")
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
                print(type(self.linklist.tail))
                removingNode = self.linklist.tail
                self.linklist.popNode(removingNode)
                self.hmap.pop(removingNode.key)
                node = LinkNode(key, value)
                self.linklist.insertBeginning(node)
                self.hmap[key] = node
                # self.linklist.print()


cache = LRUCache(3)
for i in range(1, len(nums)):
    if text[i] == "get":
        cache.get(nums[i][0])
    elif text[i] == "put":
        cache.put(nums[i][0], nums[i][1])

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(1))
# lRUCache.put(3, 3)
# print(lRUCache.get(2))
# lRUCache.put(4, 4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
