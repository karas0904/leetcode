class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen= {}
        if len(s) != len(t):
            return False
        for num in s:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1

        for num in t:
            if num in seen:
                seen[num]-=1
    
        for num in seen:
            if seen[num] != 0:
                return False
        return True