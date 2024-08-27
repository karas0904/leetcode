class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]  # Initialize the result with [-1, -1] for no occurrences
        n = len(nums)
        i = 0

        # Find the first occurrence of the target
        while i < n:
            if nums[i] == target:
                ans[0] = i  # Store the first occurrence
                break
            i += 1
        
        # Now find the last occurrence of the target
        while i < n:
            if nums[i] == target:
                ans[1] = i  # Keep updating to the last occurrence
            i += 1
        
        return ans