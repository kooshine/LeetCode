# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return
        from collections import deque
        dq = deque()
        dq.append(pRoot)
        pop_num = 1
        left_to_right = True
        result = []
        while dq:
            push_num = 0
            ret = []
            for i in range(pop_num):
                tmp = dq.popleft()
                print tmp.val
                if tmp.left:
                    dq.append(tmp.left)
                    push_num += 1
                if tmp.right:
                    dq.append(tmp.right)
                    push_num += 1
                ret.append(tmp.val)
            pop_num = push_num
            if left_to_right:
                result.append(ret)
            else:
                result.append(ret[::-1])
            ret = []
            left_to_right = not left_to_right
        return result

if __name__ == "__main__":
    tree = TreeNode(8)
    tree.left = TreeNode(10)
    tree.right = TreeNode(16)
    s = Solution()
    print s.Print(tree)

