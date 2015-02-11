def wordBreak2(s, dict): 
        if (s == ""): 
            return True 
        print 'start',s
        for i in range(1, len(s)+1): 
            if(s[:i] in dict): 
                if(marchWord(s[i:], dict)):
                    return True
        return False

def marchWord(s, dict):
        if (s == ""): 
            return True
        for i in range(1, len(s)+1): 
            if(s[:i] in dict):
                return wordBreak(s[i:], dict) 
        return False
        
def wordBreak(s, dict): 
        if (s == ""): 
            return True 
        # print 'start',s
        duplicate = [False] * (len(s)+1)
        duplicate[0] = True
        for i in range(0, len(s)): 
            if(duplicate[i] == False):
                continue
            # print i,'level'
            for j in range (i+1, len(s)+1):
                
                if(s[i:j] in dict):
                    # print s[i:j],"in",i,j,len(s)
                    duplicate[j] = True
        # print duplicate        
        return duplicate[len(s)]

s = "cars"
dicts = ["car","ca","rs"]
# print s, dicts, wordBreak(s, dicts)
# print "cars"[1:3]

s = "ab"
dicts = ["a","b"]
# print s, dicts, wordBreak(s, dicts)


s = "aaaaaaa"
dicts =  ["aaaa","aaa"]
print s, dicts, wordBreak(s, dicts)

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dicts = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print s, dicts, wordBreak(s, dicts)
# s = "leetcode"
# dicts = ["leet", "code"]
# print s, dicts, wordBreak(s, dicts)


# s = "leetcode2"
# dicts = ["leet", "code", "2"]
# print s, dicts, wordBreak(s, dicts)

# s = "abcd"
# dicts = ["abc", "bcd", "2"]
# print s, dicts, wordBreak(s, dicts)

# s = "abcd"
# dicts = ["a","abc","b","cd"]
# print s, dicts, wordBreak(s, dicts)

# s = "bbbb"
# dicts = ["b"]
# print s, dicts, wordBreak(s, dicts)

# s = "bb"
# dicts = ["a","b","abc","bbb"]
# print s, dicts, wordBreak(s, dicts)

# s = "a"
# dicts = ["a"]
# print s, dicts, wordBreak(s, dicts)

# s = "abcd"
# dicts = ["a","abc","b","cd"]
# print s, dicts, wordBreak(s, dicts)


    