# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        left_depth, right_depth = 0, 0
        is_left,is_right = False,False
        is_left = self.IsBalanced_Solution(pRoot.left)
        left_depth = self.max_depth(pRoot.left)
        is_right = self.IsBalanced_Solution(pRoot.right)
        right_depth = self.max_depth(pRoot.right)

        if abs(left_depth-right_depth) > 1:
            return False
        if is_left and is_right:
            return True

    def max_depth(self, pRoot):
        if pRoot == None:
            return 0
        left_deep = self.max_depth(pRoot.left)
        right_deep = self.max_depth(pRoot.right)
        return left_deep+1 if left_deep > right_deep else right_deep+1

