class Solution:
    # @return a tuple, (index1, index2)
    def lengthOfLongestSubstring(self, s):
        maxlen = 95
        sub = 0      
        for i in range(0, len(s)): 
            for j in range(i+1, len(s)):
                if(s[i] == s[j]):
                    if(j - i > sub):
                        sub = j - i
                        print s[i] ,i, s[j],j
                    break
                if(i > maxlen):
                    break    
            if(i > maxlen):
                break
        return sub

solution = Solution()



string = "abcabcbb"
print solution.lengthOfLongestSubstring(string)

string = "bbbbb"
print solution.lengthOfLongestSubstring(string)



string = "abcbadeigfb"
print solution.lengthOfLongestSubstring(string)

string = "abcbadeigdfb"
print solution.lengthOfLongestSubstring(string)


string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
print len(string)
print solution.lengthOfLongestSubstring(string)