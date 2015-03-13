class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        position = 0;
        if(len(A) == 0):
            return position
        for i in range(0, len(A)-1):
            # print A[i]
            if(not A[i] == A[i+1]):
                # print A[i+1]
                position += 1
                A[position] = A[i+1]
                
        print A
        return 'length:' + str(position+1)


solution = Solution()
print solution.removeDuplicates([])
print solution.removeDuplicates([1, 1])
print solution.removeDuplicates([1, 1, 1])
print solution.removeDuplicates([1, 2, 4, 4])
print solution.removeDuplicates([1, 1, 1, 2])
print solution.removeDuplicates([1, 1, 1, 1, 2, 3])
print solution.removeDuplicates([1, 2, 2 ,4, 4, 6, 6])
print solution.removeDuplicates([1, 2, 2 ,3, 4, 6, 6])