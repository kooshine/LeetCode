# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
import time
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        j = 0
        for i in range(len(popV)):
            if j < len(pushV):
                while j < len(pushV):
                    if pushV[j] != popV[i]:
                        stack.append(pushV[j])
                        j += 1
                    else:
                        j += 1
                        break
            else:
                if stack[-1] != popV[i]:
                    return False
                else:
                    stack.pop()
            print popV, pushV, stack
            time.sleep(1)
        return True if len(stack) == 0 else False

if __name__ == "__main__":
    s = Solution()
    pushV = [1,2,3,4,5]
    popV = [4,5,3,1,2]
    print s.IsPopOrder(pushV, popV)
