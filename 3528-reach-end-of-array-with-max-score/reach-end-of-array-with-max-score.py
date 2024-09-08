class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        start=0
        ans=0
        for i in range(len(nums)):
            if nums[i]>prev:
                ans+=(i-start)*nums[start]
                start=i
                prev=nums[i]
        ans+=((n-1)-start)*nums[start]
        return ans
