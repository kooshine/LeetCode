# -*- coding: utf-8 -*-
import time
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        thead = ListNode('a')
        tmp = thead
        while pHead is not None:
            while pHead and pHead.next and pHead.val == pHead.next.val:
                t = pHead.val
                while pHead and pHead.val == t:
                    pHead = pHead.next

            tmp.next = pHead
            tmp = tmp.next
            if pHead:
                pHead = pHead.next
        #return thead.next


        while thead:
            print thead.val
            thead = thead.next

if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    p = node.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(5)
    p = p.next
    p.next = ListNode(5)

    s = Solution()
    print s.deleteDuplication(node)
