class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        ans=[0]*(n+1)
        sums=0

        ans[0]=0
        for i in range(1,len(ans)):
            sums+=gain[i-1]
            ans[i]=sums
        return max(ans)
