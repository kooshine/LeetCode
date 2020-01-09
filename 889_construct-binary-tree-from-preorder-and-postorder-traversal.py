# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        N = len(pre)
        if N == 0:
            return None
        root = TreeNode(pre[0])
        if N == 1:
            return root

        L = post.index(pre[1])+1

        root.left = self.constructFromPrePost(pre[1:L+1],post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:N-1])
        return root

if __name__ == "__main__":
    s = Solution()
    print s.constructFromPrePost([1,2,4,5, 3,6,7], [4,5,2,6,7,3,1]).val
