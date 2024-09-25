class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        r=0
        maxlen=0
        
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            
            if (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            
            maxlen=max(maxlen,r-l+1)
        return maxlen



        