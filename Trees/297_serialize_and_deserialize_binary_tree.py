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
            return ""
        self.res = f"{root.val}"

        def Dfs(node: TreeNode):
            if node.left:
                self.res += f":{str(node.val)},l,{node.left.val}"
                Dfs(node.left)
            else:
                self.res += ":#"
            if node.right:
                self.res += f":{str(node.val)},r,{node.right.val}"
                Dfs(node.right)
            else:
                self.res += ":#"
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
        skip = False
        print(data)
        for i in range(1, len(nodes)):
            print(i)
            if skip:
                skip = False
                continue
            side = "l"
            cur = stack[-1]
            if nodes[i][0] == "#":
                if cur.left:
                    stack.pop()
                    continue
                if i == len(nodes)-1 or (i < len(nodes) - 1 and nodes[i+1][0] == "#"):
                    skip = True
                    stack.pop()
                    continue
                else:
                    i += 1
                    skip = True
                    side = "r"
            values = nodes[i].split(",")
            child = TreeNode(values[2])
            if side == "r" or cur.left:
                cur.right = child
            else:
                cur.left = child
            stack.append(child)

        return root


# Your Codec object will be instantiated and called as such:
# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
# print(root.left.left.val)
root = TreeNode(1)
root.right = TreeNode(2)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
# print("-----")
print(ans.val)
# print(ans.left.val)
print(ans.right.val)
# print(ans.left.left.val)
