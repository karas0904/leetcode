class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        l=0
        maxlen=0

        for r in range(len(nums)):
            if nums[r]==0:
                count+=1

            while count>1:
                if nums[l]==0:
                    count-=1
                l+=1
            
            maxlen=max(maxlen,r-l+1-count)
        return maxlen-1 if maxlen==len(nums) else maxlen


        

        