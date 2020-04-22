# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def one_path(root, path, expect):
            if root:
                path = path[:]
                path.append(root.val)
                expect -= root.val
                print path, expect
                if not root.left and not root.right and expect == 0:
                    result.append(path)
                else:
                    one_path(root.left, path, expect)
                    one_path(root.right, path, expect)
        result = []
        one_path(root, [], expectNumber)
        return result

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right = TreeNode(12)

    s = Solution()
    print s.FindPath(root, 22)
