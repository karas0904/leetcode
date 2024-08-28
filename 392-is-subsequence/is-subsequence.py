class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s=="":
            return True
        count=0
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                count+=1
                i+=1
            j+=1
            
            if count==len(s):
                return True
        return False