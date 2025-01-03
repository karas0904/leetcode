class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if arr[j]+1>arr[i]:
                        arr[i]=arr[j]+1
        maxi=0
        for i in range(len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
        return maxi

        