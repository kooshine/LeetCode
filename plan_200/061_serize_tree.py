# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        def pre(root):
            if root is None:
                ser.append("#!")
                return
            ser.append(str(root.val) + "!")
            print ser
            pre(root.left)
            pre(root.right)
        ser = []
        pre(root)
        return "".join(ser)

    def Deserialize(self, s):
        # write code here
        def pre():
            self.flag += 1
            if self.flag >= len(s):
                return None
            root = None
            if (s[self.flag] != "#"):
                root = TreeNode(int(s[self.flag]))
                root.left = pre()
                root.right = pre()
            return root
        s = s.split("!")
        print s
        return pre()

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    ret = s.Serialize(root)
    root = s.Deserialize(ret)
    if root:
        print root.val
        print root.left.val
        print root.right.val
