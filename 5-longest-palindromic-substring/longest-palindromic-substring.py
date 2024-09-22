class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_centre(left: int, right: int) -> str:
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

            if not s:
                return ""
        
        longest = ""
        for i in range(len(s)):
            odd_length=expand_around_centre(i,i)
            even_length=expand_around_centre(i,i+1)
            #used key=len so that the max funtion does not compare the lexicographically as the strings are passed not the length in int
            longest=max(longest,odd_length,even_length,key=len)
        return longest

