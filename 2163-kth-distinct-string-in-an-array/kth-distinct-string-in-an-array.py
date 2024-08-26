class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={ }
        for stri in arr:
            if stri in dic:
                dic[stri]+=1
            else:
                dic[stri]=1
        
        for stri,value in dic.items():
            if value==1:
                k-=1
                if k==0:
                    return stri
        return ""
        