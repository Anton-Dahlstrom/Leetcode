# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        self.res = f"{root.val}"

        def Dfs(node: TreeNode):
            if node.left:
                self.res += f":{str(node.val)},l,{node.left.val}"
                Dfs(node.left)
            if node.right:
                self.res += f":{str(node.val)},r,{node.right.val}"
                Dfs(node.right)
        Dfs(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(":")
        root = TreeNode(nodes[0])
        stack = [root]
        for node in nodes[1:]:
            values = node.split(",")
            parent = values[0]
            side = values[1]
            child = TreeNode(values[2])
            while stack:
                cur = stack[-1]
                if parent == cur.val:
                    stack.append(child)
                    if side == "l":
                        cur.left = child
                    else:
                        cur.right = child
                    break
                else:
                    stack.pop()
        return root


# Your Codec object will be instantiated and called as such:
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
print(root.left.left.val)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans.left.left.val)
