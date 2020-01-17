# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def build_tree(self, pre, post):
        if len(pre_order) == 0:
            return None
        root_val = pre_order[0]


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)

        helper(root)
        return result

if __name__ == "__main__":
    tree = TreeNode(1)
