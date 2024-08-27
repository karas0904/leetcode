class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]  
        n = len(nums)
        i = 0

       
        while i < n:
            if nums[i] == target:
                ans[0] = i  
                break
            i += 1
        
       
        while i < n:
            if nums[i] == target:
                ans[1] = i  
            i += 1
        
        return ans