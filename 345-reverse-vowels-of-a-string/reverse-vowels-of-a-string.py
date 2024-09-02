class Solution:
    def reverseVowels(self, s: str) -> str:
        string='aeiouAEIOU'
        total=string
        n=len(s)

        l=0
        r=n-1

        s=list(s)
        if len(s) == 2 and (s[l] in total) and (s[r] in total):
            s[l], s[r] = s[r], s[l] 
            return ''.join(s)

        while l<r:
            if s[l] in total and s[r] in total:
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                l+=1
                r-=1
            elif s[l] not in total:
                l+=1
            elif s[r] not in total:
                r-=1
        return ''.join(s)



        