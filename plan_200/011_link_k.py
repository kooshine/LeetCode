# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #注意边界的处理
        if head is None:
            return head
        node = head
        for i in range(k):
            #边界处理
            if node is None:
                return None
            node = node.next
        start = head
        while node is not None:
            start= start.next
            node = node.next
        return start
