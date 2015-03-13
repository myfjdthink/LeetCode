class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # 先排序再找中间值，简单的思路。
        C = sorted(A + B)
        if not C: return None 
        median = int(len(C)/2)-1
        if (len(C) % 2 == 1):
            return C[median + 1]
        else:
            return (float(C[median] + C[median + 1]))/2
