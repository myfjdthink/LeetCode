class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dicts = {}
        for i in range (0, len(num)):
            # 如果这个数刚好在字典里, 说明它是之前某个数字的解，则返回结果。
            if(num[i] in dicts):
                print num[i], num[dicts[num[i]]]
                j = dicts[num[i]]
                return (min(i,j) + 1, max(i,j) + 1)
            # 把当前数字与目标值target 存起来, 作为这个数字的解。
            else:
                dicts[target-num[i]] = i
