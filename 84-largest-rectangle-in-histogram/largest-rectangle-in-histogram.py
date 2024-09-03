class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        def pse(nums):
            stack=[]
            ans=[-1]*len(nums)
            for i in range(len(nums)):
                while (stack and nums[stack[-1]]>=nums[i]):
                    n=stack.pop()
                if stack:
                    ans[i]=stack[-1]        
                stack.append(i)
            return ans 
        def nse(nums):
            stack=[]
            ans = [len(nums)] * len(nums)
            for i in range(len(nums)-1,-1,-1):
                while (stack and nums[stack[-1]]>=nums[i]):
                    n=stack.pop()
                if stack:
                    ans[i]=stack[-1]        
                stack.append(i)
            return ans 
        def result(nums):
            pse_indices=pse(nums)
            nse_indices=nse(nums)
            maxi=0

            for i in range(len(nums)):
                width = nse_indices[i] - pse_indices[i] - 1
                area = nums[i] * width  
                maxi = max(maxi, area)
            return maxi
        return result(nums)
        

        

        