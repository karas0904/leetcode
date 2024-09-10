class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        add = sum(nums)
    
        if add < target:
            return 0
        
        l = 0
        r = 0
        sums = 0
        minlen = len(nums) + 1
        
        while r < len(nums):
            sums += nums[r]
            r += 1
            while sums >= target:
                minlen = min(minlen, r - l)
                sums -= nums[l]
                l += 1
        
        return minlen