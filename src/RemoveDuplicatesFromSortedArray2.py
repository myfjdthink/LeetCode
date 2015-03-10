class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if(len(A) == 0 or len(A) == 1):
            return len(A)
        position = 0;
        for i in range(0, len(A)-2):
            if(not (A[i] == A[i+1] and A[i+1] == A[i+2])):
                position += 1
                A[position] = A[i+1]
                position += 1
                A[position] = A[i+2]
        print A
        return 'length:' + str(position+2)


solution = Solution()
print solution.removeDuplicates([1,1,1,2,2,3])
print solution.removeDuplicates([1, 1, 1, 2])
print solution.removeDuplicates([1, 1, 1, 1, 2, 3])

print solution.removeDuplicates([])
print solution.removeDuplicates([1])
print solution.removeDuplicates([1, 1])
print solution.removeDuplicates([1, 1, 1])
print solution.removeDuplicates([1, 1, 1, 1])
print solution.removeDuplicates([1, 1, 1, 1, 1])
print solution.removeDuplicates([1, 2, 4, 4])
print solution.removeDuplicates([1, 2, 2 ,4, 4, 6, 6])
print solution.removeDuplicates([1, 2, 2 ,2, 4, 6, 6])


1,1,1,2,2,3
1,1,2,2,2,3
1,1,2,2,2,3
1,1,2,2,2,3