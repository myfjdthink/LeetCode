class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
            return (sum(set(A))*3 - sum(A))/2


solution = Solution()


num = [2,2,3,2]
print solution.singleNumber(num)


num = [2,2,3,2,3,3,4]
print solution.singleNumber(num)