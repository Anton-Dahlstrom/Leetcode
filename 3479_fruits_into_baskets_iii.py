class SegmentTreeMax:
    def __init__(self, arr):
        self.Tree = [0] * (len(arr)*4)
        self.build(arr, 1, 0, len(arr)-1)
        self.n = len(arr)

    def build(self, arr, treeNode, l, r):
        if l == r:
            self.Tree[treeNode] = arr[l]
        else:
            mid = l + ((r-l)//2)
            self.build(arr, treeNode*2, l, mid)
            self.build(arr, treeNode*2+1, mid+1, r)
            self.Tree[treeNode] = max(self.Tree[treeNode*2],
                                      self.Tree[treeNode*2+1])

    def query(self, l, r, treeNode=1, tl=0, tr=None):
        if tr is None:
            tr = self.n-1
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.Tree[treeNode]
        mid = tl + ((tr-tl)//2)
        return max(self.query(l, min(r, mid), treeNode*2, tl, mid),
                   self.query(max(l, mid+1), r, treeNode*2+1, mid+1, tr))

    def getMid(self, s, e):
        return s + (e - s) // 2

    def updateValue(self, arr, index, value, node=1, ss=0, se=None):
        if se == None:
            se = self.n-1
        if (index < ss or index > se):
            return

        if (ss == se):
            arr[index] = value
            self.Tree[node] = value
        else:
            mid = self.getMid(ss, se)

            if (index >= ss and index <= mid):
                self.updateValue(arr, index,
                                 value, 2 * node, ss, mid)
            else:
                self.updateValue(arr,
                                 index, value, 2 * node + 1, mid+1, se)

            self.Tree[node] = max(self.Tree[2 * node],
                                  self.Tree[2 * node + 1])
        return


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        tree = SegmentTreeMax(baskets)
        res = 0
        # binary search segment tree for first occurance of basket >= fruit
        for fruit in fruits:
            l, r = 0, n-1
            if tree.query(l, r) < fruit:
                res += 1
                continue
            while l < r:
                mid = l + ((r-l)//2)
                if tree.query(l, mid) >= fruit:
                    r = mid
                else:
                    l = mid+1
            tree.updateValue(baskets, r, 0)
        return res


fruits = [4, 2, 5]
baskets = [3, 5, 4]
output = 1

obj = Solution()
res = obj.numOfUnplacedFruits(fruits, baskets)
print(res)
print(output)
print(res == output)
