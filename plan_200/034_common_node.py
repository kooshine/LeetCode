# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        node1 = pHead1
        node2 = pHead2
        while node1 != node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1
        return node1
        """
        while pHead2 is not None:
            tmp = pHead1
            while tmp is not None:
                if tmp.val == pHead2.val:
                    return tmp
                tmp = tmp.next
            pHead2 = pHead2.next
        """
