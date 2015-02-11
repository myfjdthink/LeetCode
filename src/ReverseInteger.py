class Solution:
    # @return an integer
    def reverse(self, x):
        answer =  int(str(abs(x))[::-1])
        maxint = 2147483647
        if(answer < maxint):
            return answer * (1 if x > 0 else -1)
        else:
            return 0
solution = Solution()



num = 1534236469
print solution.reverse(num)

num = -1534236469
print solution.reverse(num)

num = -123
print solution.reverse(num)

num = 10100
print solution.reverse(num)