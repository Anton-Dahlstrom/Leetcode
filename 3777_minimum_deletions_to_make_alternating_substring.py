
class TreeNode:
    def __init__(self, li: int, ri: int):
        self.leftIndex = li
        self.rightIndex = ri
        self.leftNode = None
        self.rightNode = None
        self.deletions = 0


class Tree:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = TreeNode(0, len(arr)-1)
        self.createTree(self.root)
    # needs to set

    def createTree(self, node: TreeNode):
        if node.leftIndex != node.rightIndex:
            mid = node.leftIndex + ((node.rightIndex - node.leftIndex)//2)
            node.leftNode = TreeNode(node.leftIndex, mid)
            node.deletions += self.createTree(node.leftNode)
            node.rightNode = TreeNode(mid+1, node.rightIndex)
            node.deletions += self.createTree(node.rightNode)
            node.deletions += self.combineNodes(node.leftNode, node.rightNode)
        return node.deletions

    def query(self, node: TreeNode, start: int, end: int):
        # query covers node
        if start <= node.leftIndex and end >= node.rightIndex:
            return node.deletions
        # query misses node:
        if start > node.rightIndex or end < node.leftIndex:
            return 0
        # query covers part of the node so we search further
        res = 0
        res += self.query(node.leftNode, start, end)
        res += self.query(node.rightNode, start, end)
        # we only combine if the query hits both child nodes
        if start <= node.leftNode.rightIndex and end >= node.rightNode.leftIndex:
            res += self.combineNodes(node.leftNode, node.rightNode)
        return res

    def combineNodes(self, leftNode: TreeNode, rightNode: TreeNode):
        if self.arr[leftNode.rightIndex] == self.arr[rightNode.leftIndex]:
            return 1
        return 0

    def updateValue(self, index: int):
        if self.arr[index] == "A":
            self.arr[index] = "B"
        else:
            self.arr[index] = "A"
        self.dfsUpdate(self.root, index)

    def dfsUpdate(self, node: TreeNode, index: int):
        # if change misses this node, return deletions
        if index < node.leftIndex or index > node.rightIndex:
            return node.deletions
        # if it's a bottom node, return 0
        if node.leftIndex == node.rightIndex:
            return 0
        # nodes deletions needs to be updated
        newDeletions = 0
        newDeletions += self.dfsUpdate(node.leftNode, index)
        newDeletions += self.dfsUpdate(node.rightNode, index)
        newDeletions += self.combineNodes(node.leftNode, node.rightNode)
        node.deletions = newDeletions
        return node.deletions


class Solution:
    def minDeletions(self, s: str, queries: list[list[int]]) -> list[int]:
        strArr = [c for c in s]
        tree = Tree(strArr)
        res = []
        for query in queries:
            if query[0] == 1:
                tree.updateValue(query[1])
            if query[0] == 2:
                res.append(tree.query(tree.root, query[1], query[2]))

        return res


s = "BABA"
queries = [[2, 0, 3], [1, 1], [2, 1, 3]]
output = [0, 1]

obj = Solution()
res = obj.minDeletions(s, queries)
print(res)
print(output)
print(res == output)
