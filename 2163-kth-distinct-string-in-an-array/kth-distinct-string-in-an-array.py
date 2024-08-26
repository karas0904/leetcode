class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={ }
        for stri in arr:
            if stri in dic:
                dic[stri]+=1
            else:
                dic[stri]=1
        count=0
        for stri,value in dic.items():
            if value==1:
                count+=1
                if count==k:
                    return stri
        return ""
        