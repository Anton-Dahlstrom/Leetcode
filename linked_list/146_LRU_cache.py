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

# The LRU cache class uses a hashmap to quickly lookup keys.
# Each key will point to a LinkNode that will be part of a linked chain in the LinkList class.
# When a key is inserted or used it will be moved to the front of the chain and the missing connections between nodes will be closed in the popNode function.
# If the chain becomes too long (determined by the size of the cache), we will also remove the node at the end of the chain, aswell as it's connections.
# Finally if a node is removed we also pop it from the LRU hashmap.


# The key attribute will be used to find which key to remove from the LRU hashmap when we pop the tail.
# Val attribute is simply be the value that the key holds and that we return to the user.
# Next and prev are used to close the chain when we pop a node, ensuring that the nodes behind and head of the node to be popped connect to eachother.


# When we add nodes we will place them infront of the head, set their next attribute to the head and assign the linklists head attribute to the new node.
# When we pop the tail node we simply take it's previous node, set it as the linklists tail attribute and set it's self.next attribute to None.
# If a node in the middle of our list is called we pop it from the chain and insert it as the new head.

# Code doesn't work because the LinkList starts with two nodes which throws off the capacity parameter.

class LinkNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self) -> None:
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertHead(self, node: LinkNode):
        if node == None:
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def popNode(self, node: LinkNode):
        if node == None:
            return
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.next = None
            node.prev = None
            return
        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linklist = LinkList()
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.linklist.popNode(node)
            self.linklist.insertHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.linklist.popNode(node)
            self.linklist.insertHead(node)
        else:
            if self.capacity:
                self.capacity -= 1
            else:
                removingNode = self.linklist.tail
                self.linklist.popNode(removingNode)
                print("removing", removingNode.key)
                if removingNode.key is not None:
                    self.hmap.pop(removingNode.key)
            node = LinkNode(key, value)
            self.linklist.insertHead(node)
            self.hmap[key] = node


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
