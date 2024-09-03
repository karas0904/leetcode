class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        stack=[]
        left=[0]*len(height)
        right=[0]*len(height)

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        trapped_water = 0
        for i in range(n):
            water_at_index = min(left[i], right[i]) - height[i]
            if water_at_index > 0:
                trapped_water += water_at_index
        return trapped_water



        

        