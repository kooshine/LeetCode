# -*- coding: utf-8 -*-
import time
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        tq = [[root]]
        flag = 1
        while len(tq) > 0:
            level = tq.pop(0)
            tmp = []
            if flag % 2 == 1:
                for i in range(len(level)):
                    tmp.append(level[i].val)
                print "if", tmp
            else:
                for i in range(len(level)-1, -1, -1):
                    tmp.append(level[i].val)
                print "else",tmp
            result.append(tmp)
            flag += 1
            print i
            print result
            time.sleep(1)
            tmp = []
            for item in level:
                if item.left:
                    tmp.append(item.left)
                if item.right:
                    tmp.append(item.right)
            if len(tmp) > 0:
                tq.append(tmp)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    print s.zigzagLevelOrder(root)
