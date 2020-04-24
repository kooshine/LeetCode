# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        #创建新节点
        tmp = pHead
        while tmp is not None:
            new = RandomListNode(tmp.label)
            new.next = tmp.next
            tmp.next = new
            tmp = new.next
        #绑定random
        tmp = pHead
        while tmp.next.next is not None:
            if tmp.random:
                tmp.next.random = tmp.random
            tmp = tmp.next.next
        #摘出新节点
        tmp = pHead
        new = tmp.next
        new_clone = new
        while tmp is not None:
            tmp.next = new_clone.next
            tmp = tmp.next
            new_clone.next = tmp.next if tmp else None
            new_clone = new_clone.next
        return new
