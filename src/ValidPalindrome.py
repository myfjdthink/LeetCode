class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
           news = filter(str.isalnum, s)
           print news
           return news.lower() == news[::-1].lower()


solution = Solution()


strs = "A man, a plan, a canal: Panama"
print solution.isPalindrome(strs)


strs = "`l;`` 1o1 ??;l`"
print solution.isPalindrome(strs)