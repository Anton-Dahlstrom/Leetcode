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
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                self.res += f":{node.left.val}"
                stack.append(node.left)
            else:
                self.res += ":#"
            if node.right:
                self.res += f":{node.right.val}"
                stack.append(node.right)
            else:
                self.res += ":#"
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
        i = 1
        while i < len(nodes):
            cur = stack.pop(0)
            val = nodes[i]
            if val != "#":
                newNode = TreeNode(val)
                cur.left = newNode
                stack.append(newNode)
            val = nodes[i+1]
            if val != "#":
                newNode = TreeNode(val)
                cur.right = newNode
                stack.append(newNode)
            i += 2
        return root


# root = TreeNode(1)
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# print(ans.val)
