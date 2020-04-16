# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        else:
            return self.maxDepth(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1

    def maxDepth(self, left, right):
        return left if left > right else right


