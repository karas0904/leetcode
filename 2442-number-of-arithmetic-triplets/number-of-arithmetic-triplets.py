class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]+diff in nums and 2*diff+nums[i] in nums:
                count+=1
        return count