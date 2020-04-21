# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        #放在一个栈里，pop时候是不对的
        self.min_stack = [] #有序递减数组
    def push(self, node):
        # write code here
        self.stack.append(node)
        #插入有序递减数组
        for i in range(len(self.min_stack)):
            if node > self.min_stack[i]:
                self.min_stack.insert(i, node)
                return
        self.min_stack.append(node)
    def pop(self):
        # write code here
        if len(self.stack) > 0:
            top_val = self.stack.pop()
        for i in range(len(self.min_stack)):#有序数组查找、删除
            if top_val == self.min_stack[i]:
                #self.min_stack.remove(self.min_stack[i])
                del self.min_stack[i]
                return
    def top(self):
        # write code here
        if len(self.stack) <= 0:
            return None
        return self.stack[-1]
    def min(self):
        # write code here注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
        return self.min_stack[-1]

if __name__ == "__main__":
    s = Solution()
    print s.push(3)
    print s.min()
    print s.push(4)
    print s.min()
    print s.push(2)
    print s.min()
    print s.push(3)
    print s.min()
    print s.pop()
    print s.min()
    print s.pop()
    print s.min()
    print s.pop()
    print s.min()
    print s.push(0)
    print s.min()

