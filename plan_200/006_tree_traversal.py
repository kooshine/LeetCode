# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        tin_index = tin.index(pre[0])
        root.left =  self.reConstructBinaryTree(pre[1: 1+ tin_index], tin[0:tin_index])
        root.right = self.reConstructBinaryTree(pre[1+tin_index:], tin[tin_index+1:])
        return root
