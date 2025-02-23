from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root = TreeNode(preorder[0])

        def dfs(node, prel, prer, postl, postr):
            if prer-prel == 1 and postr-postl == 1:
                if preorder[prel] == postorder[postl]:
                    node.left = TreeNode(preorder[prel])
                    node.right = TreeNode(preorder[prer])
                    return
            if prel > prer or postl > postr:
                return
            if prel == prer:
                node.left = TreeNode(preorder[prel])
                return

            node.left = TreeNode(preorder[prel])
            t_pre_l = prel
            t_pre_r = prer
            t_post_l = postl
            t_post_r = postr

            if preorder[prel] != postorder[postr]:
                node.right = TreeNode(postorder[postr])
                while t_pre_r >= 0 and preorder[t_pre_r] != node.right.val:
                    t_pre_r -= 1
                t_pre_r -= 1
                while t_post_r >= 0 and postorder[t_post_r] != node.left.val:
                    t_post_r -= 1

            dfs(node.left, prel+1, t_pre_r, postl, t_post_r-1)
            if node.right:
                while t_pre_l < n and preorder[t_pre_l] != node.right.val:
                    t_pre_l += 1
                while t_post_l < n and postorder[t_post_l] != node.left.val:
                    t_post_l += 1
                dfs(node.right, t_pre_l+1, prer, t_post_l+1, postr-1)
        dfs(root, 1, n-1, 0, n-2)
        return root
