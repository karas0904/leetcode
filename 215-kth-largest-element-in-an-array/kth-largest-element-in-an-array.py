class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if i==k-1:
                return nums[i]        