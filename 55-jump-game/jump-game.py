class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_destination=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=final_destination:
                final_destination=i
        return final_destination==0
