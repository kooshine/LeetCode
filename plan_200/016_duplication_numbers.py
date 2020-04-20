# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    #numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                    # 注意这样交换会出现问题，需要先保存一个中间结果，不能直接交换，
                    # 否则当处理numbers[numbers[i]]的时候会找不到正确的下标
                    # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                    tmp = numbers[i]
                    numbers[i] = numbers[tmp]
                    numbers[tmp] = tmp
        return False
