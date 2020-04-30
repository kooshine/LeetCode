# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0:
            return
        def mid_search(pRoot):
            if pRoot is None:
                return
            mid_search(pRoot.left)
            result.append(pRoot.val)
            mid_search(pRoot.right)

        result = []
        mid_search(pRoot)

        return result[k-1] if result else None
if __name__ == "__main__":
    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(20)
    s = Solution()
    print s.KthNode(t, 1)
