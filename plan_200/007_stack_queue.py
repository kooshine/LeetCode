# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    stack_in = []
    stack_out = []
    def push(self, node):
        # write code here
        self.stack_in.append(node)
    def pop(self):
        # return xx
        if len(self.stack_out) == 0:
            length = len(self.stack_in)
            if length == 0:
                return None
            for i in range(length-1, -1, -1):
                self.stack_out.append(self.stack_in[i])

        return self.stack_out.pop()

if __name__ == "__main__":
    s = Solution()
    s.push(1)
    print s.pop()
