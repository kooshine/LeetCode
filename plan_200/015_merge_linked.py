# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        tmp = ListNode(0)
        merged = tmp
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        if pHead1 is not None:
            tmp.next = pHead1
        if pHead2 is not None:
            tmp.next = pHead2
        return merged.next
