# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) <= 0:
            return []
        low, high = 0, len(numbers)-1

    def quick_sort(self, numbers, low, high):
        if low >= high:
            print numbers
            return numbers
        base = self.divide(numbers, low, high)
        self.quick_sort(numbers, low, base-1)
        self.quick_sort(numbers, base+1, high)

    def divide(self,numbers, i,j):
        base = numbers[i]
        while i < j:
                while i < j and numbers[j] + base >= base + numbers[j]:
                    j -= 1
                numbers[i] = numbers[j]
                while i < j and numbers[i] + base <= base + numbers[i]:
                    i += 1
                numbers[j] = numbers[i]
        numbers[i] = base
        return i


if __name__ == "__main__":
    s = Solution()
    #data = raw_input()
    #data = data.strip().split(",")
    data = [2,6,0, 0]
    data =[str(item) for item in data]
    low, high = 0, len(data)-1
    s.quick_sort(data, low, high)
    print "after sort",data
