class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        C = sorted(A + B)
        if not C: return None 
        median = int(len(C)/2)-1
        if (len(C) % 2 == 1):
            return C[median + 1]
        else:
            return (float(C[median] + C[median + 1]))/2



solution = Solution()



nums1 = [2,3,4]
nums2 = [5,6,7]
print solution.findMedianSortedArrays(nums1, nums2)


nums1 = [2,3,4, 8 , 9]
nums2 = [5,6,7]
print solution.findMedianSortedArrays(nums1, nums2)

nums1 = []
nums2 = [5,6,7]
print solution.findMedianSortedArrays(nums1, nums2)

nums1 = [2]
nums2 = []
print solution.findMedianSortedArrays(nums1, nums2)

nums1 = []
nums2 = []
print solution.findMedianSortedArrays(nums1, nums2)



nums = [184.8,208.7
,193.1
,201.7
,196.7
,189.2
,196
,195.2
,180.7
,191.3
,194.5
,214.5
,192.5
,191.4
,201.2
,194
,182.5
,179.2
,192.6
,191.6
,194.8
,100.5
]

# print sum(nums)

# def counts(n, index, num, total):
#     for i in range (0, len(num)):
#         for j in range (0, len(num)):
#             print num[i],num[j]

# counts(7, 0, nums, 0)        