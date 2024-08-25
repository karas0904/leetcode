class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expected=1

        for num in nums:
            if num<=0:
                continue
            
            if num==expected:
                expected+=1
            elif num>expected:
                return expected
        return expected

