class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))

        if len(nums)<3:
            return max(nums)
        
        nums=sorted(nums, reverse=True)
        count=1
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
                if count==3:
                    return nums[i]
        return nums[0]
