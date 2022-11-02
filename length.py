class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        length = 0
        
        if i == 0:
            return len(s)
    
        while i > 0:
            if s[i]!=" ":
                length +=1
            
            if length > 0 and s[i] == " ":
                return length
            
            i -=1
            
            
            
obj = Solution()

s="   fly me   to   the moon"
print(obj.lengthOfLastWord(s))