# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        LHead = self.Convert(pRootOfTree.left)
        if LHead is None:
            LHead = pRootOfTree
        else:
            tmp = LHead
            while tmp.right is not None:
                tmp = tmp.right
            tmp.right = pRootOfTree
            pRootOfTree.left = tmp

        RHead = self.Convert(pRootOfTree.right)
        if RHead:
            RHead.left = pRootOfTree
            pRootOfTree.right = RHead
        return LHead
