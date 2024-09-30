class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==1:
            return max(nums[0],nums[1])
        
        prev1=nums[0]
        prev2=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            current=max(prev2,nums[i]+prev1)
            prev1,prev2=prev2,current
        return prev2

        