class Solution:
    # @return an integer
    def romanToInt(self, s):
        if(s is None):
            return 0

        charToInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre = 0
        answer =  0
        for i in range(len(s)-1,-1 ,-1):
            present = charToInt[s[i]]
            if(pre <= present):
                answer += present
            else:
                answer -= present
            pre = present

        return answer

solution = Solution()

print solution.romanToInt("")#0

print solution.romanToInt("IV")#4

print solution.romanToInt("DCCC")#800

print solution.romanToInt("XVII")#17

print solution.romanToInt("CMXCIX")#999

print solution.romanToInt("MDCCCXCIX")#1899

print solution.romanToInt("MMMCMXCIX")#3999


