# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        m = len(numbers)
        self.sort(numbers, 0, m-1)
        total_0 = 0

        for i in range(m-1):
            if numbers[i] == 0:
                total_0 += 1
                continue
            if numbers[i+1] == numbers[i] and numbers[i] != 0:
                return False
            need = numbers[i+1]-numbers[i] - 1
            if need > 0:
                total_0 = total_0 - need
                if total_0 < 0:
                    return False
        return True

    def sort(self, numbers, i , j):
        if i >= j:
            return numbers
        mid = self.divide(numbers, i, j)
        print mid
        self.sort(numbers, i, mid-1)
        self.sort(numbers, mid+1, j)

    def divide(self, numbers, i, j):
        base = numbers[i]
        while i < j:
            while numbers[j] >= base and i < j:
                j -= 1
            numbers[i] = numbers[j]
            while numbers[i] <= base and i < j:
                i += 1
            numbers[j] = numbers[i]
        numbers[i] = base
        return i

if __name__ == "__main__":
    s = Solution()
    print s.IsContinuous([2,6, 0, 0])
