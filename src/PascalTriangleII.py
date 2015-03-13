import math

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        out = []
        if(numRows == 0):
            return out
        if(numRows == 1):
            return [[1]]
        for i in range(0, numRows):
            inner = []
            for j in range(0, i+1):
                #print self.factorial(i)/(self.factorial(j) * self.factorial(i-j)),
                inner.append(self.factorial(i)/(self.factorial(j) * self.factorial(i-j)))
            # print
            out.append(inner)
        return out


    def generate2(self, rowIndex):
        if(rowIndex == 0):
            return []
        if(rowIndex == 1):
            return [1]
        inner = []
        for j in range(0, rowIndex+1):
            #print self.factorial(i)/(self.factorial(j) * self.factorial(i-j)),
            inner.append(self.factorial(rowIndex)/(self.factorial(j) * self.factorial(rowIndex-j)))
        return inner


    def factorial(self, n, nums=1):
        n = n or 1
        return nums if n == 1 else self.factorial(n-1, nums*n)



solution = Solution()



# print solution.generate(1)

print solution.generate(5)


print solution.generate2(1)

# print solution.factorial(0)