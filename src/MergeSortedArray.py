class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    # Copy
    # 这个题目的要求是不能对 A 进行修改
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        for num in range(m, m+n):
            A.insert(num, 0)

        #move bigest to the end
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1

        return A

solution = Solution()

print solution.merge([1,2,5], 3, [3, 4, 6, 7, 8], 5)#0

print solution.merge([], 0, [1], 1)#0

print solution.merge([1,2,4,5,6], 5, [3], 1)


