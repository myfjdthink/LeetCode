class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin1(self, num):
        for i in range(0, len(num)-1):
            if(num[i] > num[i+1]):
                return num[i+1]
        return num[0]

    def findMin2(self, num):
        mini = num[0]
        if(len(num) < 3):
            return min(num)
        point = int(len(num)/2)
        # num[point] is the min
        if( num[point] < num[point-1] and num[point] < mini):
            mini =  num[point]
        other = self.findMin(num[0:point]) if num[point] <= num[0] else self.findMin(num[point:])
        return min(mini, other)

    def findMin(self, num):
        i = 0
        j = len(num)-1
        while(i < j-1):
            point = int((i + j)/2)
            if(num[point] >= num[i]):
                i = point
            if(num[point] <= num[j]):
                j = point
        return min(num[0], num[i], num[point], num[j])

solution = Solution()

# nums = [1]
# print solution.findMin(nums)

# nums = [1, 2]
# print solution.findMin(nums)

# nums = [1, 2, 0]
# print solution.findMin(nums)

# nums = [4, 5, 6, 7, 0, 1, 2]
# print solution.findMin(nums)

# nums = [1,2,3,4,5]
# print solution.findMin(nums)

# nums = [4, 5, 6, 7, 8, 1, 2]
# # print solution.findMin(nums)

# nums = [5, 6, 7, 1, 2, 2, 4]
# print solution.findMin(nums)

# nums = [ 6, 7, 8, 9,  3, 4, 5]
# print solution.findMin(nums)

nums = [ 3, 1, 1]
print solution.findMin(nums)

nums = [3,3,1,3]
print solution.findMin(nums)

nums = [3,3,1,3,3]
print solution.findMin(nums)


