class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        s=list(s)

        for i in range(len(s)):
            dic={}
            for j in range(i,len(s)):
                if s[j] in dic and dic[s[j]] == 1:
                    break
                leng=j-i+1
                maxlen=max(maxlen,leng)
                dic[s[j]]=1
        return maxlen
        