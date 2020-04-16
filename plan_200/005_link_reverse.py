# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    三种思路
    递归
    先读出来，反转
    放在栈里，然后pop
"""

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ret = []
        while listNode is not None:
            ret.append(listNode.val)
            listNode = listNode.next
        tmp = []
        for i in range(len(ret)-1, -1, -1):
            tmp.append(ret[i])
        return tmp


"""
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    resutl = []
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        def test(listNode):
            if listNode is  not None:
                test(listNode.next)
                result.append(listNode.val)
            return result
        return test(listNode)
"""
